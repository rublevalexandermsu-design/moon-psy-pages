
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
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.46;
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x151c26);
scene.fog = new THREE.FogExp2(0x0c121b, 0.0037);

const camera = new THREE.PerspectiveCamera(54, 1, 0.1, 120);
camera.position.set(0, 1.2, 5.5);

scene.add(new THREE.HemisphereLight(0xf3ffff, 0x47291a, 1.58));
scene.add(new THREE.AmbientLight(0xfff0d8, 0.38));
const warm = new THREE.PointLight(0xffcf86, 4.1, 62);
warm.position.set(0, 5, -18);
scene.add(warm);
const cool = new THREE.PointLight(0x8cebff, 1.95, 52);
cool.position.set(-4, 3, -38);
scene.add(cool);

const loader = new THREE.TextureLoader();
const clickable = [];
const frames = [];
const panelLights = [];
const artworkLights = [];

function mat(color, roughness = 0.8, metalness = 0.05) {
  return new THREE.MeshStandardMaterial({ color, roughness, metalness });
}

function makeTexture(size, painter, repeatX = 1, repeatY = 1) {
  const c = document.createElement('canvas');
  c.width = size;
  c.height = size;
  const ctx = c.getContext('2d');
  painter(ctx, size);
  const texture = new THREE.CanvasTexture(c);
  texture.colorSpace = THREE.SRGBColorSpace;
  texture.wrapS = THREE.RepeatWrapping;
  texture.wrapT = THREE.RepeatWrapping;
  texture.repeat.set(repeatX, repeatY);
  texture.anisotropy = Math.min(renderer.capabilities.getMaxAnisotropy?.() || 8, 8);
  return texture;
}

function createParquetTexture() {
  return makeTexture(1024, (ctx, size) => {
    const bg = ctx.createLinearGradient(0, 0, size, size);
    bg.addColorStop(0, '#2a1a10');
    bg.addColorStop(0.5, '#6b4425');
    bg.addColorStop(1, '#23150d');
    ctx.fillStyle = bg;
    ctx.fillRect(0, 0, size, size);
    const plank = 128;
    for (let y = -plank; y < size + plank; y += plank) {
      for (let x = -plank; x < size + plank; x += plank) {
        ctx.save();
        ctx.translate(x + plank / 2, y + plank / 2);
        ctx.rotate(((x + y) / plank) % 2 ? Math.PI / 4 : -Math.PI / 4);
        const g = ctx.createLinearGradient(-plank / 2, 0, plank / 2, 0);
        g.addColorStop(0, '#2d1b0f');
        g.addColorStop(0.45, '#8b5d34');
        g.addColorStop(1, '#3a2313');
        ctx.fillStyle = g;
        ctx.fillRect(-plank / 2, -plank / 5, plank, plank / 2.4);
        ctx.strokeStyle = 'rgba(246,196,118,.20)';
        ctx.lineWidth = 3;
        ctx.strokeRect(-plank / 2, -plank / 5, plank, plank / 2.4);
        for (let i = 0; i < 11; i += 1) {
          ctx.strokeStyle = `rgba(255,221,165,${0.035 + i * 0.004})`;
          ctx.beginPath();
          ctx.moveTo(-plank / 2 + i * 13, -plank / 5);
          ctx.bezierCurveTo(-30 + i * 12, -12, 12 + i * 6, 16, plank / 2, plank / 5 - i);
          ctx.stroke();
        }
        ctx.restore();
      }
    }
    const shine = ctx.createRadialGradient(size * 0.55, size * 0.42, 10, size * 0.55, size * 0.42, size * 0.5);
    shine.addColorStop(0, 'rgba(255,231,174,.34)');
    shine.addColorStop(0.45, 'rgba(255,231,174,.08)');
    shine.addColorStop(1, 'rgba(255,231,174,0)');
    ctx.fillStyle = shine;
    ctx.fillRect(0, 0, size, size);
  }, 5, 22);
}

function createWallTexture() {
  return makeTexture(1024, (ctx, size) => {
    const bg = ctx.createLinearGradient(0, 0, size, size);
    bg.addColorStop(0, '#162636');
    bg.addColorStop(0.55, '#0f1b27');
    bg.addColorStop(1, '#091019');
    ctx.fillStyle = bg;
    ctx.fillRect(0, 0, size, size);
    for (let x = 80; x < size; x += 220) {
      ctx.fillStyle = 'rgba(255,226,172,.045)';
      ctx.fillRect(x, 0, 4, size);
      ctx.fillStyle = 'rgba(0,0,0,.18)';
      ctx.fillRect(x + 6, 0, 8, size);
    }
    for (let y = 130; y < size; y += 230) {
      ctx.fillStyle = 'rgba(255,226,172,.035)';
      ctx.fillRect(0, y, size, 4);
      ctx.fillStyle = 'rgba(0,0,0,.16)';
      ctx.fillRect(0, y + 6, size, 7);
    }
    for (let i = 0; i < 6500; i += 1) {
      const alpha = Math.random() * 0.035;
      ctx.fillStyle = `rgba(255,255,255,${alpha})`;
      ctx.fillRect(Math.random() * size, Math.random() * size, 1, 1);
    }
  }, 1, 8);
}

function createCeilingTexture() {
  return makeTexture(1024, (ctx, size) => {
    ctx.fillStyle = '#0c0d11';
    ctx.fillRect(0, 0, size, size);
    for (let x = 0; x < size; x += 240) {
      for (let y = 0; y < size; y += 240) {
        const g = ctx.createRadialGradient(x + 120, y + 120, 8, x + 120, y + 120, 130);
        g.addColorStop(0, 'rgba(255,218,150,.10)');
        g.addColorStop(1, 'rgba(0,0,0,.10)');
        ctx.fillStyle = g;
        ctx.fillRect(x, y, 240, 240);
        ctx.strokeStyle = 'rgba(216,170,93,.18)';
        ctx.lineWidth = 8;
        ctx.strokeRect(x + 20, y + 20, 200, 200);
        ctx.strokeStyle = 'rgba(0,0,0,.42)';
        ctx.lineWidth = 10;
        ctx.strokeRect(x + 36, y + 36, 168, 168);
      }
    }
  }, 2, 10);
}

function createSheenTexture() {
  return makeTexture(512, (ctx, size) => {
    ctx.clearRect(0, 0, size, size);
    const g = ctx.createLinearGradient(0, 0, size, size);
    g.addColorStop(0, 'rgba(255,255,255,0)');
    g.addColorStop(0.46, 'rgba(255,255,255,.20)');
    g.addColorStop(0.52, 'rgba(255,226,172,.12)');
    g.addColorStop(1, 'rgba(255,255,255,0)');
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, size, size);
  }, 1, 1);
}

function loadSceneTexture(path, repeatX = 1, repeatY = 1) {
  const texture = loader.load(path);
  texture.colorSpace = THREE.SRGBColorSpace;
  texture.wrapS = THREE.RepeatWrapping;
  texture.wrapT = THREE.RepeatWrapping;
  texture.repeat.set(repeatX, repeatY);
  texture.anisotropy = Math.min(renderer.capabilities.getMaxAnisotropy?.() || 8, 8);
  return texture;
}

function makeBox(w, h, d, material, x, y, z) {
  const mesh = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), material);
  mesh.position.set(x, y, z);
  scene.add(mesh);
  return mesh;
}

const parquetTexture = loadSceneTexture('assets/scene/gallery-floor-parquet.webp', 1.8, 11);
const wallTexture = createWallTexture();
const panelTexture = loadSceneTexture('assets/scene/gallery-wall-panel-texture.webp', 1, 1);
const ceilingTexture = loadSceneTexture('assets/scene/gallery-ceiling-coffered.webp', 1.6, 8);
const sheenTexture = createSheenTexture();
const wallMat = new THREE.MeshStandardMaterial({ color: 0x122232, map: wallTexture, bumpMap: wallTexture, bumpScale: 0.018, roughness: 0.76, metalness: 0.04 });
const panelMat = new THREE.MeshStandardMaterial({ color: 0xffffff, map: panelTexture, bumpMap: panelTexture, bumpScale: 0.018, roughness: 0.68, metalness: 0.06 });
const floorMat = new THREE.MeshStandardMaterial({ color: 0xffffff, map: parquetTexture, bumpMap: parquetTexture, bumpScale: 0.055, roughness: 0.38, metalness: 0.18 });
const ceilingMat = new THREE.MeshStandardMaterial({ color: 0xffffff, map: ceilingTexture, bumpMap: ceilingTexture, bumpScale: 0.025, roughness: 0.64, metalness: 0.08 });
const floor = new THREE.Mesh(new THREE.PlaneGeometry(19, 82, 32, 160), floorMat);
floor.rotation.x = -Math.PI / 2;
floor.position.set(0, -2.24, -34);
floor.receiveShadow = true;
scene.add(floor);
makeBox(19, 0.16, 82, mat(0x160e08, 0.7, 0.08), 0, -2.42, -34);
makeBox(19, 0.2, 82, ceilingMat, 0, 5.2, -34);
makeBox(0.25, 7.5, 82, wallMat, -9.5, 1.35, -34);
makeBox(0.25, 7.5, 82, wallMat, 9.5, 1.35, -34);
makeBox(19, 7.5, 0.25, mat(0x111018, 0.75, 0.08), 0, 1.35, -74);

function makeSideWallPanel(side, z) {
  const isLeft = side === 'left';
  const x = isLeft ? -9.31 : 9.31;
  const normalOffset = isLeft ? 0.05 : -0.05;
  const panel = new THREE.Mesh(new THREE.PlaneGeometry(5.15, 5.15), panelMat);
  panel.position.set(x + normalOffset, 1.1, z);
  panel.rotation.y = isLeft ? Math.PI / 2 : -Math.PI / 2;
  scene.add(panel);
  const trim = mat(0xb48138, 0.38, 0.55);
  makeBox(0.055, 5.45, 0.08, trim, x + normalOffset * 1.8, 1.1, z - 2.72);
  makeBox(0.055, 5.45, 0.08, trim, x + normalOffset * 1.8, 1.1, z + 2.72);
  makeBox(0.055, 0.08, 5.45, trim, x + normalOffset * 1.8, 3.82, z);
  makeBox(0.055, 0.08, 5.45, trim, x + normalOffset * 1.8, -1.62, z);
  const lights = [];
  [-1.45, 0, 1.45].forEach((offset) => {
    const lampGlow = new THREE.PointLight(0xffd89a, 0.62, 8.5);
    lampGlow.position.set(x + (isLeft ? 0.72 : -0.72), 3.32, z + offset);
    scene.add(lampGlow);
    lights.push(lampGlow);
    const lamp = new THREE.Mesh(new THREE.CylinderGeometry(0.08, 0.13, 0.16, 18), mat(0xd8aa5d, 0.34, 0.62));
    lamp.rotation.z = Math.PI / 2;
    lamp.position.set(x + (isLeft ? 0.16 : -0.16), 3.38, z + offset);
    scene.add(lamp);
  });
  panelLights.push({ z, lights });
}

artworks.forEach((art) => {
  if (art.scene.x < -1) makeSideWallPanel('left', art.scene.z);
  if (art.scene.x > 1) makeSideWallPanel('right', art.scene.z);
});

for (let z = -8; z > -72; z -= 8) {
  const light = new THREE.PointLight(0xffcf86, 1.85, 25);
  light.position.set(0, 4.3, z);
  scene.add(light);
  makeBox(17.4, 0.08, 0.16, mat(0x5a3e24, 0.45, 0.44), 0, 5.05, z);
  makeBox(0.08, 5.2, 0.12, mat(0x6f4c2a, 0.48, 0.36), -9.28, 1.35, z + 2.4);
  makeBox(0.08, 5.2, 0.12, mat(0x6f4c2a, 0.48, 0.36), 9.28, 1.35, z + 2.4);
  const spot = new THREE.Mesh(new THREE.CylinderGeometry(0.13, 0.2, 0.09, 24), mat(0xf4c878, 0.32, 0.6));
  spot.position.set(0, 5.0, z + 1.8);
  spot.rotation.x = Math.PI / 2;
  scene.add(spot);
}

const doorGroup = new THREE.Group();
const doorMat = mat(0x1b1513, 0.48, 0.24);
const leftDoor = makeBox(4.8, 6.2, 0.28, doorMat, -2.4, 1, 2.2);
const rightDoor = makeBox(4.8, 6.2, 0.28, doorMat, 2.4, 1, 2.2);
doorGroup.add(leftDoor, rightDoor);
scene.add(doorGroup);

function makeBench(x, z) {
  const bench = new THREE.Group();
  const seatMat = new THREE.MeshStandardMaterial({ color: 0x061225, roughness: 0.42, metalness: 0.16 });
  const seat = new THREE.Mesh(new THREE.BoxGeometry(3.2, 0.34, 0.86, 8, 2, 4), seatMat);
  seat.position.set(0, 0, 0);
  seat.castShadow = true;
  bench.add(seat);
  const trimMat = mat(0xb48138, 0.36, 0.58);
  const frontTrim = new THREE.Mesh(new THREE.BoxGeometry(3.28, 0.08, 0.05), trimMat);
  frontTrim.position.set(0, -0.03, 0.46);
  bench.add(frontTrim);
  const backTrim = frontTrim.clone();
  backTrim.position.z = -0.46;
  bench.add(backTrim);
  for (let ix = -1; ix <= 1; ix += 1) {
    for (let iz = -1; iz <= 1; iz += 2) {
      const tuft = new THREE.Mesh(new THREE.SphereGeometry(0.16, 18, 8), mat(0x020814, 0.52, 0.08));
      tuft.scale.set(1.15, 0.13, 0.72);
      tuft.position.set(ix * 0.82, 0.20, iz * 0.22);
      bench.add(tuft);
    }
  }
  [-0.42, 0.42].forEach((lineZ) => {
    const seam = new THREE.Mesh(new THREE.BoxGeometry(3.0, 0.025, 0.025), mat(0x1d2f4b, 0.48, 0.08));
    seam.position.set(0, 0.19, lineZ);
    bench.add(seam);
  });
  const legMat = mat(0x8b642e, 0.42, 0.5);
  [[-1.25, -0.25], [1.25, -0.25], [-1.25, 0.25], [1.25, 0.25]].forEach(([lx, lz]) => {
    const leg = new THREE.Mesh(new THREE.CylinderGeometry(0.055, 0.085, 0.62, 18), legMat);
    leg.position.set(lx, -0.48, lz);
    bench.add(leg);
    const foot = new THREE.Mesh(new THREE.SphereGeometry(0.105, 18, 10), legMat);
    foot.scale.set(0.9, 0.42, 0.9);
    foot.position.set(lx, -0.82, lz);
    bench.add(foot);
  });
  bench.position.set(x, -1.37, z);
  scene.add(bench);
  return bench;
}
makeBench(-4.7, -7.2);
makeBench(4.7, -7.2);

function textTexture(title, subtitle) {
  const c = document.createElement('canvas');
  c.width = 2200; c.height = 820;
  const ctx = c.getContext('2d');
  const bg = ctx.createLinearGradient(0, 0, c.width, c.height);
  bg.addColorStop(0, '#101722');
  bg.addColorStop(0.55, '#07101a');
  bg.addColorStop(1, '#171018');
  ctx.fillStyle = bg;
  ctx.fillRect(0, 0, c.width, c.height);
  ctx.strokeStyle = '#d8aa5d';
  ctx.lineWidth = 10;
  ctx.strokeRect(28, 28, c.width - 56, c.height - 56);
  ctx.strokeStyle = 'rgba(255,235,180,.32)';
  ctx.lineWidth = 3;
  ctx.strokeRect(52, 52, c.width - 104, c.height - 104);
  ctx.fillStyle = '#f4d38a';
  ctx.font = '800 94px Georgia';
  ctx.textAlign = 'center';
  ctx.textBaseline = 'alphabetic';
  wrap(ctx, title, c.width / 2, 220, 1680, 104);
  ctx.fillStyle = '#f0eaf0';
  ctx.font = '600 50px Segoe UI';
  wrap(ctx, subtitle, c.width / 2, 500, 1760, 68);
  const texture = new THREE.CanvasTexture(c);
  texture.colorSpace = THREE.SRGBColorSpace;
  texture.generateMipmaps = false;
  texture.minFilter = THREE.LinearFilter;
  texture.magFilter = THREE.LinearFilter;
  texture.anisotropy = Math.min(renderer.capabilities.getMaxAnisotropy?.() || 8, 16);
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
  t.anisotropy = Math.min(renderer.capabilities.getMaxAnisotropy?.() || 8, 8);
  const imageMat = new THREE.MeshStandardMaterial({
    map: t,
    bumpMap: t,
    displacementMap: t,
    emissive: 0xffffff,
    emissiveMap: t,
    emissiveIntensity: 0.16,
    bumpScale: 0.065,
    displacementScale: art.shape === 'round' ? 0.035 : 0.026,
    roughness: 0.46,
    metalness: 0.03,
  });
  const w = art.scene.width;
  const h = art.scene.height;
  const plane = new THREE.Mesh(new THREE.PlaneGeometry(w, h, 72, 72), imageMat);
  plane.position.z = 0.04;
  plane.castShadow = true;
  plane.userData.art = art;
  group.add(plane);
  clickable.push(plane);
  const sheen = new THREE.Mesh(
    new THREE.PlaneGeometry(w, h),
    new THREE.MeshBasicMaterial({ map: sheenTexture, transparent: true, opacity: 0.18, blending: THREE.AdditiveBlending, depthWrite: false }),
  );
  sheen.position.z = 0.072;
  group.add(sheen);

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
  const plaqueWidth = Math.min(4.35, w + 1.16);
  const isMainPedestal = art.placement === 'pedestal';
  const isCenterWork = art.placement === 'center';
  const plaqueHeight = isMainPedestal ? 0.84 : 0.92;
  const plaqueY = isMainPedestal ? -h / 2 - 0.16 : (isCenterWork ? -h / 2 - 0.58 : -h / 2 - 0.46);
  const plaqueZ = isMainPedestal ? 1.18 : (isCenterWork ? 0.26 : 0.16);
  const plaqueBack = new THREE.Mesh(new THREE.BoxGeometry(plaqueWidth + 0.16, plaqueHeight + 0.18, 0.12), mat(0x0f1118, 0.45, 0.38));
  plaqueBack.position.set(0, plaqueY, plaqueZ - 0.05);
  group.add(plaqueBack);
  const plaque = new THREE.Mesh(new THREE.PlaneGeometry(plaqueWidth, plaqueHeight), new THREE.MeshBasicMaterial({ map: plaqueTexture, toneMapped: false }));
  plaque.position.set(0, plaqueY, plaqueZ + 0.03);
  group.add(plaque);

  if (isMainPedestal) {
    const pedestalMat = mat(0x1a1210, 0.36, 0.42);
    const pedestal = new THREE.Mesh(new THREE.CylinderGeometry(w * 0.48, w * 0.56, 0.82, 72), pedestalMat);
    pedestal.position.set(0, -h / 2 - 0.72, 0.0);
    pedestal.castShadow = true;
    group.add(pedestal);
    [-0.32, -1.08].forEach((rimY) => {
      const rim = new THREE.Mesh(new THREE.TorusGeometry(w * 0.50, 0.028, 10, 72), mat(0xd8aa5d, 0.32, 0.68));
      rim.rotation.x = Math.PI / 2;
      rim.position.set(0, -h / 2 + rimY, 0.0);
      group.add(rim);
    });
  }

  group.position.set(art.scene.x, art.scene.y, art.scene.z);
  group.rotation.y = THREE.MathUtils.degToRad(art.scene.ry);
  group.userData.baseY = group.position.y;
  group.userData.index = index;
  const focusLight = new THREE.PointLight(0xffddb0, 0.38, 9.5);
  focusLight.position.set(0, h / 2 + 0.78, 1.15);
  group.add(focusLight);
  artworkLights.push({ group, light: focusLight });
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
  sample.pos.y += Math.sin(current * Math.PI * 18) * 0.034 + Math.sin(performance.now() * 0.0013) * 0.006;
  camera.position.copy(sample.pos);
  camera.lookAt(sample.look);
  const door = Math.min(1, current / 0.11);
  leftDoor.rotation.y = -door * 1.25;
  rightDoor.rotation.y = door * 1.25;
  panelLights.forEach(({ z, lights }) => {
    const focus = Math.max(0, 1 - Math.abs(z - camera.position.z) / 8.5);
    lights.forEach((light) => {
      light.intensity = 0.68 + focus * 2.45;
      light.distance = 7.5 + focus * 3.5;
    });
  });
  frames.forEach((group, index) => {
    const distance = Math.abs(group.position.z - camera.position.z);
    const active = distance < 7;
    group.position.y = group.userData.baseY;
    group.scale.setScalar(active ? 1.012 : 1);
  });
  artworkLights.forEach(({ group, light }) => {
    const focus = Math.max(0, 1 - Math.abs(group.position.z - camera.position.z) / 7.2);
    light.intensity = 0.52 + focus * 2.35;
  });
  renderer.render(scene, camera);
}
animate();
