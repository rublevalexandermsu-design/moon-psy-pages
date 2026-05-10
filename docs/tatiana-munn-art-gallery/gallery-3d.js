
import * as THREE from './assets/vendor/three.module.min.js';

const canvas = document.getElementById('galleryCanvas');
const dataNode = document.getElementById('artworksData');
const artworks = JSON.parse(dataNode?.textContent || '[]');
const meter = document.getElementById('scrollMeter');
const modal = document.getElementById('artModal');
const modalImage = document.getElementById('modalImage');
const modalTitle = document.getElementById('modalTitle');
const modalText = document.getElementById('modalText');
const modalDetail = document.getElementById('modalDetail');
const flipCard = document.getElementById('flipCard');
const flipButton = document.getElementById('flipButton');

const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: false, powerPreference: 'high-performance' });
renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.5));
renderer.outputColorSpace = THREE.SRGBColorSpace;

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x0a0d13);
scene.fog = new THREE.FogExp2(0x080c14, 0.006);

const camera = new THREE.PerspectiveCamera(54, 1, 0.1, 120);
camera.position.set(0, 1.2, 5.5);

scene.add(new THREE.HemisphereLight(0xd7f6ff, 0x24130d, 1.0));
const warm = new THREE.PointLight(0xffc56f, 2.25, 48);
warm.position.set(0, 5, -18);
scene.add(warm);
const cool = new THREE.PointLight(0x5fd6df, 1.45, 40);
cool.position.set(-4, 3, -38);
scene.add(cool);

const loader = new THREE.TextureLoader();
const clickable = [];
const frames = [];

function mat(color, roughness = 0.8, metalness = 0.05) {
  return new THREE.MeshStandardMaterial({ color, roughness, metalness });
}

function makeBox(w, h, d, material, x, y, z) {
  const mesh = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), material);
  mesh.position.set(x, y, z);
  scene.add(mesh);
  return mesh;
}

const wallMat = mat(0x303945, 0.62, 0.08);
const floorMat = mat(0x4a2f1d, 0.42, 0.28);
makeBox(19, 0.2, 82, floorMat, 0, -2.35, -34);
for (let z = 1; z > -73; z -= 4) {
  makeBox(0.035, 0.03, 82, mat(0x7b5330, 0.55, 0.24), -7.2 + ((z + 73) % 16), -2.22, -34);
}
makeBox(19, 0.2, 82, mat(0x10131b, 0.85, 0.03), 0, 5.2, -34);
makeBox(0.25, 7.5, 82, wallMat, -9.5, 1.35, -34);
makeBox(0.25, 7.5, 82, wallMat, 9.5, 1.35, -34);
makeBox(19, 7.5, 0.25, mat(0x111018, 0.75, 0.08), 0, 1.35, -74);

for (let z = -8; z > -72; z -= 8) {
  const light = new THREE.PointLight(0xffcf86, 1.0, 18);
  light.position.set(0, 4.3, z);
  scene.add(light);
  makeBox(17.4, 0.08, 0.16, mat(0x4d3521, 0.5, 0.45), 0, 5.05, z);
}

const doorGroup = new THREE.Group();
const doorMat = mat(0x1b1513, 0.48, 0.24);
const leftDoor = makeBox(4.8, 6.2, 0.28, doorMat, -2.4, 1, 2.2);
const rightDoor = makeBox(4.8, 6.2, 0.28, doorMat, 2.4, 1, 2.2);
doorGroup.add(leftDoor, rightDoor);
scene.add(doorGroup);

function makeBench(x, z) {
  const seat = makeBox(3.1, 0.32, 0.78, mat(0x071326, 0.38, 0.22), x, -1.42, z);
  const legMat = mat(0x8b642e, 0.42, 0.5);
  [[-1.25, -0.25], [1.25, -0.25], [-1.25, 0.25], [1.25, 0.25]].forEach(([lx, lz]) => {
    makeBox(0.12, 0.72, 0.12, legMat, x + lx, -1.88, z + lz);
  });
  return seat;
}
makeBench(-4.7, -7.2);
makeBench(4.7, -7.2);

function textTexture(title, subtitle) {
  const c = document.createElement('canvas');
  c.width = 1024; c.height = 420;
  const ctx = c.getContext('2d');
  ctx.fillStyle = '#11151d';
  ctx.fillRect(0, 0, c.width, c.height);
  ctx.strokeStyle = '#d8aa5d';
  ctx.lineWidth = 6;
  ctx.strokeRect(18, 18, c.width - 36, c.height - 36);
  ctx.fillStyle = '#f4d38a';
  ctx.font = '54px Georgia';
  ctx.textAlign = 'center';
  wrap(ctx, title, c.width / 2, 120, 820, 58);
  ctx.fillStyle = '#d6ccd7';
  ctx.font = '30px Segoe UI';
  wrap(ctx, subtitle, c.width / 2, 270, 860, 38);
  const texture = new THREE.CanvasTexture(c);
  texture.colorSpace = THREE.SRGBColorSpace;
  return texture;
}

function wrap(ctx, text, x, y, maxWidth, lineHeight) {
  const words = String(text).split(' ');
  let line = '';
  for (const word of words) {
    const test = line ? line + ' ' + word : word;
    if (ctx.measureText(test).width > maxWidth && line) {
      ctx.fillText(line, x, y);
      line = word; y += lineHeight;
    } else line = test;
  }
  ctx.fillText(line, x, y);
}

function addArtwork(art, index) {
  const group = new THREE.Group();
  const t = loader.load(art.image);
  t.colorSpace = THREE.SRGBColorSpace;
  const imageMat = new THREE.MeshBasicMaterial({ map: t });
  const w = art.scene.width;
  const h = art.scene.height;
  const plane = new THREE.Mesh(new THREE.PlaneGeometry(w, h), imageMat);
  plane.position.z = 0.04;
  plane.userData.art = art;
  group.add(plane);
  clickable.push(plane);

  const frameMat = mat(0x18100c, 0.42, 0.55);
  const frameThickness = 0.12;
  const frameDepth = 0.16;
  const topFrame = new THREE.Mesh(new THREE.BoxGeometry(w + frameThickness * 2, frameThickness, frameDepth), frameMat);
  const bottomFrame = topFrame.clone();
  const leftFrame = new THREE.Mesh(new THREE.BoxGeometry(frameThickness, h + frameThickness * 2, frameDepth), frameMat);
  const rightFrame = leftFrame.clone();
  topFrame.position.set(0, h / 2 + frameThickness / 2, -0.04);
  bottomFrame.position.set(0, -h / 2 - frameThickness / 2, -0.04);
  leftFrame.position.set(-w / 2 - frameThickness / 2, 0, -0.04);
  rightFrame.position.set(w / 2 + frameThickness / 2, 0, -0.04);
  group.add(topFrame, bottomFrame, leftFrame, rightFrame);
  frames.push(group);

  const plaqueTexture = textTexture(art.title, art.intent);
  const plaqueWidth = Math.min(3.9, w + 1.0);
  const plaqueY = (art.placement === 'pedestal' || art.placement === 'center') ? -h / 2 - 0.38 : -h / 2 - 0.76;
  const plaqueZ = (art.placement === 'pedestal' || art.placement === 'center') ? 0.72 : 0.12;
  const plaqueBack = new THREE.Mesh(new THREE.BoxGeometry(plaqueWidth + 0.16, 1.0, 0.1), mat(0x0f1118, 0.52, 0.36));
  plaqueBack.position.set(0, plaqueY, plaqueZ - 0.05);
  group.add(plaqueBack);
  const plaque = new THREE.Mesh(new THREE.PlaneGeometry(plaqueWidth, 0.82), new THREE.MeshBasicMaterial({ map: plaqueTexture }));
  plaque.position.set(0, plaqueY, plaqueZ + 0.03);
  group.add(plaque);

  if (art.placement === 'pedestal' || art.placement === 'center') {
    const pedestal = new THREE.Mesh(new THREE.CylinderGeometry(w * 0.42, w * 0.5, 0.8, 48), mat(0x1a1210, 0.42, 0.38));
    pedestal.position.set(0, -h / 2 - 0.64, -0.28);
    group.add(pedestal);
  }

  group.position.set(art.scene.x, art.scene.y, art.scene.z);
  group.rotation.y = THREE.MathUtils.degToRad(art.scene.ry);
  group.userData.baseY = group.position.y;
  group.userData.index = index;
  scene.add(group);
}

artworks.forEach(addArtwork);

const raycaster = new THREE.Raycaster();
const pointer = new THREE.Vector2();
canvas.addEventListener('click', event => {
  const rect = canvas.getBoundingClientRect();
  pointer.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
  pointer.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;
  raycaster.setFromCamera(pointer, camera);
  const hit = raycaster.intersectObjects(clickable, false)[0];
  if (hit?.object?.userData?.art) openArt(hit.object.userData.art);
});

document.querySelector('[data-preview-art]')?.addEventListener('click', () => openArt(artworks[0]));
document.querySelectorAll('[data-close-art]').forEach(el => el.addEventListener('click', closeArt));
flipButton?.addEventListener('click', () => {
  flipCard.classList.toggle('is-flipped');
  flipButton.textContent = flipCard.classList.contains('is-flipped') ? 'На лицевую сторону' : 'Перевернуть';
});

function openArt(art) {
  modalImage.src = art.image;
  modalImage.alt = art.title;
  modalTitle.textContent = art.title;
  modalText.textContent = `${art.note} ${art.intent}`;
  modalDetail.href = art.detailUrl;
  document.getElementById('purchaseArtwork').value = art.title;
  flipCard.classList.remove('is-flipped');
  flipButton.textContent = 'Перевернуть';
  modal.setAttribute('aria-hidden', 'false');
}
function closeArt() { modal.setAttribute('aria-hidden', 'true'); }

function resize() {
  const w = window.innerWidth;
  const h = window.innerHeight;
  camera.aspect = w / h;
  camera.updateProjectionMatrix();
  renderer.setSize(w, h, false);
}
window.addEventListener('resize', resize);
resize();

function scrollProgress() {
  const max = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
  return Math.min(1, Math.max(0, window.scrollY / max));
}

let target = 0;
let current = 0;
const heroSection = document.querySelector('.hero-section');
const sideSections = [...document.querySelectorAll('.story-section.side-copy')];

function smooth(t) {
  const v = Math.max(0, Math.min(1, t));
  return v * v * (3 - 2 * v);
}

function viewForArt(art) {
  const isLeft = art.scene.x < -1;
  const isRight = art.scene.x > 1;
  const isCenter = !isLeft && !isRight;
  const cameraX = isLeft ? art.scene.x + 3.85 : isRight ? art.scene.x - 3.85 : 0;
  const cameraZ = art.scene.z + (isCenter ? 6.7 : 4.25);
  const cameraY = isCenter ? 0.74 : 0.92;
  return {
    p: 0,
    pos: new THREE.Vector3(cameraX, cameraY, cameraZ),
    look: new THREE.Vector3(art.scene.x, art.scene.y - 0.86, art.scene.z),
  };
}

const cameraStops = [
  { p: 0.00, pos: new THREE.Vector3(0, 1.15, 5.6), look: new THREE.Vector3(0, 1.0, -8) },
  { p: 0.08, pos: new THREE.Vector3(0, 1.1, 1.6), look: new THREE.Vector3(0, 0.7, -8) },
  ...artworks.map((art, index) => {
    const stop = viewForArt(art);
    stop.p = 0.15 + index * 0.068;
    return stop;
  }),
  { p: 0.88, pos: new THREE.Vector3(0, 1.2, -63), look: new THREE.Vector3(0, 0.4, -72) },
  { p: 1.00, pos: new THREE.Vector3(0, 1.45, -70), look: new THREE.Vector3(0, 0.5, -74) },
];

function cameraSample(progress) {
  for (let i = 0; i < cameraStops.length - 1; i += 1) {
    const a = cameraStops[i];
    const b = cameraStops[i + 1];
    if (progress <= b.p) {
      const t = smooth((progress - a.p) / Math.max(0.001, b.p - a.p));
      return {
        pos: a.pos.clone().lerp(b.pos, t),
        look: a.look.clone().lerp(b.look, t),
      };
    }
  }
  return cameraStops[cameraStops.length - 1];
}

function updateStoryPanels(progress) {
  if (heroSection) {
    const heroOpacity = 1 - smooth((progress - 0.025) / 0.055);
    heroSection.style.opacity = Math.max(0, Math.min(1, heroOpacity)).toFixed(3);
    heroSection.style.pointerEvents = heroOpacity > 0.35 ? 'auto' : 'none';
  }
  const panelWindows = [
    [0.115, 0.185],
    [0.245, 0.315],
    [0.500, 0.570],
    [0.785, 0.855],
  ];
  sideSections.forEach((section, index) => {
    const [start, end] = panelWindows[index] || [1, 1];
    const fadeIn = smooth((progress - start) / 0.02);
    const fadeOut = 1 - smooth((progress - (end - 0.02)) / 0.02);
    const opacity = Math.max(0, Math.min(1, fadeIn, fadeOut));
    section.style.opacity = opacity.toFixed(3);
    section.style.pointerEvents = opacity > 0.45 ? 'auto' : 'none';
  });
}

function animate() {
  requestAnimationFrame(animate);
  target = scrollProgress();
  current += (target - current) * 0.12;
  if (meter) meter.style.width = `${current * 100}%`;
  document.documentElement.style.setProperty('--entry-open', String(Math.min(1, target / 0.075).toFixed(3)));
  updateStoryPanels(current);
  const sample = cameraSample(current);
  sample.pos.y += Math.sin(current * Math.PI * 18) * 0.025;
  camera.position.copy(sample.pos);
  camera.lookAt(sample.look);
  const door = Math.min(1, current / 0.11);
  leftDoor.rotation.y = -door * 1.25;
  rightDoor.rotation.y = door * 1.25;
  frames.forEach((group, index) => {
    const distance = Math.abs(group.position.z - camera.position.z);
    const active = distance < 7;
    group.position.y = group.userData.baseY + Math.sin(performance.now() * 0.001 + index) * (active ? 0.05 : 0.015);
    group.scale.setScalar(active ? 1.04 : 1);
  });
  renderer.render(scene, camera);
}
animate();
