
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
scene.background = new THREE.Color(0x080b12);
scene.fog = new THREE.FogExp2(0x080c14, 0.010);

const camera = new THREE.PerspectiveCamera(54, 1, 0.1, 120);
camera.position.set(0, 1.2, 5.5);

scene.add(new THREE.HemisphereLight(0xd7f6ff, 0x24130d, 0.82));
const warm = new THREE.PointLight(0xffc56f, 1.9, 42);
warm.position.set(0, 5, -18);
scene.add(warm);
const cool = new THREE.PointLight(0x5fd6df, 1.25, 36);
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

const wallMat = mat(0x1b222b, 0.72, 0.1);
const floorMat = mat(0x211810, 0.62, 0.18);
makeBox(19, 0.2, 82, floorMat, 0, -2.35, -34);
makeBox(19, 0.2, 82, mat(0x10131b, 0.85, 0.03), 0, 5.2, -34);
makeBox(0.25, 7.5, 82, wallMat, -9.5, 1.35, -34);
makeBox(0.25, 7.5, 82, wallMat, 9.5, 1.35, -34);
makeBox(19, 7.5, 0.25, mat(0x111018, 0.75, 0.08), 0, 1.35, -74);

for (let z = -8; z > -72; z -= 8) {
  const light = new THREE.PointLight(0xffcf86, 0.78, 16);
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
  const plaque = new THREE.Mesh(new THREE.PlaneGeometry(Math.min(3.6, w + 0.8), 0.85), new THREE.MeshBasicMaterial({ map: plaqueTexture }));
  plaque.position.set(0, -h / 2 - 0.7, 0.08);
  group.add(plaque);

  if (art.placement === 'pedestal' || art.placement === 'center') {
    const pedestal = new THREE.Mesh(new THREE.CylinderGeometry(w * 0.42, w * 0.5, 0.8, 48), mat(0x1a1210, 0.42, 0.38));
    pedestal.position.set(0, -h / 2 - 0.52, -0.18);
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
function animate() {
  requestAnimationFrame(animate);
  target = scrollProgress();
  current += (target - current) * 0.06;
  if (meter) meter.style.width = `${current * 100}%`;
  const z = 5.5 - current * 74;
  const x = Math.sin(current * Math.PI * 4.8) * 2.0;
  camera.position.set(x, 1.05 + Math.sin(current * Math.PI * 8) * 0.08, z);
  camera.rotation.y = Math.sin(current * Math.PI * 4.8) * -0.09;
  camera.rotation.x = -0.035;
  const door = Math.min(1, current / 0.08);
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
