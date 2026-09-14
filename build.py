import base64

with open('lib/assets/ak-emblem-core.png', 'rb') as f:
    em_core = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('ascii')
with open('lib/assets/ak-emblem-wing.png', 'rb') as f:
    em_wing = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('ascii')
with open('lib/assets/ak-emblem-cube.png', 'rb') as f:
    em_cube = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('ascii')

with open('lib/assets/ak-sub-bg.png', 'rb') as f:
    bg_b64 = base64.b64encode(f.read()).decode('ascii')

with open('lib/assets/ak-emblem-send.png', 'rb') as f:
    em_send = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('ascii')

with open('lib/assets/ak-emblem-stop.png', 'rb') as f:
    em_stop = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('ascii')

css = """/* ── 明日方舟·罗德岛皮肤 — 官网设计语言 + HUD 动效层 ── */

/* 1) 调色板 */
body[data-dsh-arknights] {
  color-scheme: dark;
  --dsw-alias-bg-base: rgba(10, 11, 13, 0.38);
  --dsw-alias-bg-layer-1: rgba(13, 15, 18, 0.58);
  --dsw-alias-bg-layer-2: rgba(16, 19, 23, 0.52);
  --dsw-alias-bg-layer-3: rgba(19, 23, 27, 0.48);
  --dsw-alias-bg-mask-1: rgba(4, 6, 9, 0.3);
  --dsw-alias-bg-module-platform: rgba(10, 11, 13, 0.45);
  --dsw-alias-border-l1: rgba(255, 255, 255, 0.1);
  --dsw-alias-border-l2: rgba(255, 255, 255, 0.16);
  --dsw-alias-border-l3: rgba(53, 200, 245, 0.4);
  --dsw-alias-border-l4: rgba(53, 200, 245, 0.65);
  --dsw-alias-label-primary: #f4f7f9;
  --dsw-alias-label-primary-foreground: #0a0b0d;
  --dsw-alias-label-primary-inverted: #0a0b0d;
  --dsw-alias-label-secondary: rgba(244, 247, 249, 0.82);
  --dsw-alias-label-tertiary: rgba(244, 247, 249, 0.6);
  --dsw-alias-label-caption: rgba(244, 247, 249, 0.48);
  --dsw-alias-label-dimmed: rgba(244, 247, 249, 0.4);
  --dsw-alias-brand-primary: #35c8f5;
  --dsw-alias-link: #35c8f5;
  --dsw-alias-button-primary-fill: #35c8f5;
  --dsw-alias-button-primary-hover: #5cd4f7;
  --dsw-alias-button-contrast-fill: #0a0b0d;
  --dsw-alias-button-ghost-active-border: rgba(53, 200, 245, 0.55);
  --dsw-alias-button-ghost-active-fill: rgba(53, 200, 245, 0.14);
  --dsw-alias-button-tool-bar-fill: rgba(13, 15, 18, 0.72);
  --dsw-alias-button-tool-bar-hover: rgba(255, 255, 255, 0.08);
  --dsw-alias-interactive-bg-hover: rgba(255, 255, 255, 0.07);
  --dsw-alias-interactive-bg-active: rgba(53, 200, 245, 0.16);
  --dsw-alias-interactive-bg-hover-danger: rgba(239, 68, 68, 0.16);
  --dsw-alias-markdown-code-block: rgba(12, 14, 17, 0.92);
  --dsw-alias-markdown-inline-code: rgba(53, 200, 245, 0.14);
  --dsw-alias-markdown-tag: rgba(53, 200, 245, 0.78);
  --dsw-alias-scrollbar-thumb: rgba(255, 255, 255, 0.24);
  --dsw-alias-scrollbar-bg-l2: rgba(255, 255, 255, 0.04);
  --dsw-alias-state-success-primary: #22c55e;
  --dsw-alias-state-success-tertiary: rgba(34, 197, 94, 0.16);
  --dsw-alias-state-error-primary: #ef4444;
  --dsw-alias-state-warn-primary: #ffd902;
  --dsw-alias-state-warn-label: #ffd902;
  --dsw-alias-state-warn-tertiary: rgba(255, 217, 2, 0.15);
  --dsw-alias-state-business-primary: #35c8f5;
  --dsw-alias-hovercard-bg: rgba(16, 18, 21, 0.96);
  --dsw-alias-tooltip-bg: rgba(16, 18, 21, 0.96);

  /* shadcn 风格变量（侧栏/面板同时在用的另一套） */
  --background: #0a0b0d;
  --foreground: #f4f7f9;
  --card: rgba(16, 18, 21, 0.78);
  --card-foreground: #f4f7f9;
  --popover: #14171a;
  --popover-foreground: #f4f7f9;
  --primary: #35c8f5;
  --primary-foreground: #0a0b0d;
  --secondary: #14171a;
  --secondary-foreground: #f4f7f9;
  --muted: #14171a;
  --muted-foreground: rgba(244, 247, 249, 0.62);
  --accent: rgba(53, 200, 245, 0.14);
  --accent-foreground: #f4f7f9;
  --border: rgba(255, 255, 255, 0.12);
  --input: rgba(255, 255, 255, 0.14);
  --ring: #35c8f5;
  --sidebar: #0b0c0e;
  --sidebar-foreground: #f2f5f7;
  --sidebar-primary: #35c8f5;
  --sidebar-primary-foreground: #0a0b0d;
  --sidebar-accent: rgba(53, 200, 245, 0.14);
  --sidebar-accent-foreground: #f4f7f9;
  --sidebar-border: rgba(255, 255, 255, 0.1);
  --sidebar-ring: #35c8f5;
  background: transparent !important;
}

/* 2) 全局直角 */
body[data-dsh-arknights] * {
  border-radius: 0 !important;
}

/* 3) 侧栏 */
body[data-dsh-arknights] [data-slot='sidebar'],
body[data-dsh-arknights] [class*='sidebarCol'] {
  background: linear-gradient(180deg, rgba(11, 12, 14, 0.74) 0%, rgba(16, 19, 21, 0.66) 100%) !important;
  backdrop-filter: blur(6px);
}

body[data-dsh-arknights] [data-slot='sidebar'] :is(span, div, p, a, button, h1, h2, h3, h4, label, li) {
  color: rgba(242, 245, 247, 0.88) !important;
}

body[data-dsh-arknights] [data-slot='sidebar'] :is(input, textarea) {
  background: rgba(255, 255, 255, 0.06) !important;
  border: 1px solid rgba(255, 255, 255, 0.14) !important;
  color: #f2f5f7 !important;
}

body[data-dsh-arknights] [data-slot='sidebar'] ::placeholder {
  color: rgba(242, 245, 247, 0.4) !important;
}

body[data-dsh-arknights] [data-slot='sidebar'] button[class*='newSession'] {
  background: rgba(53, 200, 245, 0.1) !important;
  border: 1px solid rgba(53, 200, 245, 0.4) !important;
  transition: background 0.2s ease, border-color 0.2s ease;
}

body[data-dsh-arknights] [data-slot='sidebar'] button[class*='newSession']:hover {
  background: rgba(53, 200, 245, 0.22) !important;
  border-color: rgba(53, 200, 245, 0.8) !important;
}

body[data-dsh-arknights] [data-slot='sidebar'] [class*='newSession'] span,
body[data-dsh-arknights] [data-slot='sidebar'] [class*='newSession'] > * {
  background: transparent !important;
  border: none !important;
}

body[data-dsh-arknights] [data-slot='sidebar'] [class*='newSession'] > * {
  background: transparent !important;
}

body[data-dsh-arknights] [data-slot='sidebar'] [class*='fade'] {
  background: linear-gradient(rgba(11, 12, 14, 0), #0b0c0e) !important;
}

/* 3.8) 聊天气泡：用户消息气泡暗色化（硬编码浅蓝底的组件） */
body[data-dsh-arknights] [class*='bubble'] {
  background: rgba(53, 200, 245, 0.09) !important;
  color: #f4f7f9 !important;
}

body[data-dsh-arknights] [class*='bubble'] :is(span, div, p) {
  color: inherit !important;
}

/* 3.9) 全局选中态：data-active 元素统一青色高亮（菜单/标签/导航） */
body[data-dsh-arknights] [data-active='true'] {
  background: rgba(53, 200, 245, 0.12) !important;
  color: #f4f7f9 !important;
}

/* 4) 输入卡：极简 AK 面板语言 — 细线边框 + 顶部青色强调线 */
body[data-dsh-arknights] [data-composer-card] {
  position: relative;
  background: rgba(12, 14, 17, 0.72) !important;
  border: 1px solid rgba(255, 255, 255, 0.13) !important;
  border-radius: 2px !important;
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.42) !important;
  backdrop-filter: blur(10px);
  transition: border-color 0.25s ease, box-shadow 0.25s ease;
}

/* 顶部强调线：青色，聚焦时点亮 */
body[data-dsh-arknights] [data-composer-card]::before {
  content: '';
  position: absolute;
  top: -1px;
  left: 0;
  width: 34%;
  height: 2px;
  background: rgba(53, 200, 245, 0.4);
  transition: width 0.3s ease, background 0.3s ease, box-shadow 0.3s ease;
  pointer-events: none;
}

body[data-dsh-arknights] [data-composer-card]:focus-within {
  border-color: rgba(53, 200, 245, 0.4) !important;
  box-shadow: 0 6px 28px rgba(0, 0, 0, 0.5) !important;
}

body[data-dsh-arknights] [data-composer-card]:focus-within::before {
  width: 100%;
  background: #35c8f5;
  box-shadow: 0 0 10px rgba(53, 200, 245, 0.55);
}

body[data-dsh-arknights] [data-composer-card] button[class*='_add'] {
  background: rgba(255, 255, 255, 0.07) !important;
}

body[data-dsh-arknights] [data-composer-card] button[class*='_add']:hover {
  background: rgba(53, 200, 245, 0.18) !important;
}

body[data-dsh-arknights] [data-composer-card] button[class*='_primary'] {
  background: url(__EMBLEM_SEND__) center/contain no-repeat !important;
  border: none !important;
  box-shadow: none !important;
  transform: scale(1.18);
  transition: transform 0.18s ease, filter 0.18s ease;
  filter: drop-shadow(0 0 6px rgba(53, 200, 245, 0.45));
}

body[data-dsh-arknights] [data-composer-card] button[class*='_primary'] svg {
  display: none !important;
}

body[data-dsh-arknights] [data-composer-card] button[class*='_primary']:hover {
  background: url(__EMBLEM_SEND__) center/contain no-repeat !important;
  box-shadow: none !important;
  transform: scale(1.3);
  filter: drop-shadow(0 0 12px rgba(53, 200, 245, 0.75)) brightness(1.25);
}

body[data-dsh-arknights] [data-composer-card] button[class*='_primary']:active {
  transform: scale(1.08);
}

/* 停止态（生成中）：JS 扫描器切换 data-ak-stop，菱形徽章 */
body[data-dsh-arknights] [data-composer-card] button[class*='_primary'][data-ak-stop] {
  background: url(__EMBLEM_STOP__) center/82% no-repeat !important;
  animation: ak-stop-pulse 1.6s ease-in-out infinite;
}

@keyframes ak-stop-pulse {
  0%, 100% { filter: drop-shadow(0 0 4px rgba(53, 200, 245, 0.4)); }
  50% { filter: drop-shadow(0 0 10px rgba(53, 200, 245, 0.85)); }
}

body[data-dsh-arknights] [data-composer-card] button[class*='_primary'][data-ak-stop]:hover {
  background: url(__EMBLEM_STOP__) center/82% no-repeat !important;
  transform: scale(1.24);
}

/* 5) cordis 面板/行 */
body[data-dsh-arknights] [data-cordis-panel] {
  background: rgba(13, 15, 18, 0.5) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  backdrop-filter: blur(8px);
  color: #f4f7f9;
}

body[data-dsh-arknights] [data-cordis-panel] > header {
  background: rgba(255, 255, 255, 0.04) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
}

body[data-dsh-arknights] [data-cordis-row] {
  background: rgba(255, 255, 255, 0.03) !important;
}

body[data-dsh-arknights] [data-cordis-row]:hover {
  background: rgba(53, 200, 245, 0.08) !important;
}

body[data-dsh-arknights] ::selection {
  background: rgba(53, 200, 245, 0.4);
}

body[data-dsh-arknights] ::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.22) !important;
}

body[data-dsh-arknights] a {
  color: #35c8f5;
}

/* 5.5) 设置弹窗深度美化：导航 / 徽章 / 表单 / 滚动条 */
/* 导航单元格：hover 淡青，选中 = 青色左条 + 淡青底 + 亮青字（覆盖写死的 rgb(235,238,242)） */
body[data-dsh-arknights] [class*='navCell'] {
  background: transparent !important;
  color: rgba(244, 247, 249, 0.82) !important;
  border: 1px solid transparent !important;
  transition: background 0.18s ease, color 0.18s ease, border-color 0.18s ease;
}

body[data-dsh-arknights] [class*='navCell']:hover {
  background: rgba(53, 200, 245, 0.08) !important;
  color: #d9f3fc !important;
}

body[data-dsh-arknights] [class*='navCell'][class*='active'],
body[data-dsh-arknights] [class*='navCell'][aria-current='true'] {
  background: rgba(53, 200, 245, 0.14) !important;
  border-color: rgba(53, 200, 245, 0.4) !important;
  color: #7fdcff !important;
  box-shadow: inset 2px 0 0 #35c8f5;
}

/* 「当前使用」等浅色徽章 → 青色系 */
body[data-dsh-arknights] [class*='inUse'],
body[data-dsh-arknights] span[class*='_tag_'] {
  background: rgba(53, 200, 245, 0.13) !important;
  color: #7fdcff !important;
  border: 1px solid rgba(53, 200, 245, 0.4) !important;
  border-radius: 2px;
}

/* 原生 select 下拉（上下文页等）：深色化 */
body[data-dsh-arknights] select {
  background: rgba(14, 17, 21, 0.85) !important;
  color: #f4f7f9 !important;
  border: 1px solid rgba(255, 255, 255, 0.14) !important;
  border-radius: 2px;
}

body[data-dsh-arknights] select option {
  background: #101418;
  color: #f4f7f9;
}

/* 弹窗内输入框统一深色 */
body[data-dsh-arknights] [data-cordis-panel] input:not([type='checkbox']):not([type='radio']),
body[data-dsh-arknights] [data-cordis-panel] textarea {
  background: rgba(255, 255, 255, 0.05) !important;
  border: 1px solid rgba(255, 255, 255, 0.14) !important;
  color: #f4f7f9 !important;
  border-radius: 2px;
}

body[data-dsh-arknights] [data-cordis-panel] input::placeholder {
  color: rgba(244, 247, 249, 0.35);
}

/* 5.6) 设置弹窗容器：实体化面板，解决透明度太高的问题 */
body[data-dsh-arknights] [class*='Aa_panel'],
body[data-dsh-arknights] [class*='overlay'] [class*='panel'] {
  background: rgba(14, 17, 21, 0.93) !important;
  backdrop-filter: blur(18px);
  border: 1px solid rgba(255, 255, 255, 0.13) !important;
  box-shadow: 0 24px 90px rgba(0, 0, 0, 0.75) !important;
  border-radius: 3px;
}

body[data-dsh-arknights] [class*='Aa_mask'],
body[data-dsh-arknights] [class*='overlay'] [class*='mask'] {
  background: rgba(2, 3, 5, 0.48) !important;
  backdrop-filter: blur(3px);
}

/* 5.7) 全局滚动条：细深色条 + 青色悬浮 */
body[data-dsh-arknights] * {
  scrollbar-width: thin;
  scrollbar-color: rgba(53, 200, 245, 0.35) transparent;
}

body[data-dsh-arknights] *::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

body[data-dsh-arknights] *::-webkit-scrollbar-track {
  background: transparent;
}

body[data-dsh-arknights] *::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.14);
  border-radius: 4px;
}

body[data-dsh-arknights] *::-webkit-scrollbar-thumb:hover {
  background: rgba(53, 200, 245, 0.5);
}

/* 弹窗内容底色加深，保证浮层可读性 */
body[data-dsh-arknights] [data-cordis-panel] {
  box-shadow: 0 24px 80px rgba(0, 0, 0, 0.65) !important;
}

/* 轨迹页搜索框等全局输入边框调暗 */
body[data-dsh-arknights] {
  --input: rgba(255, 255, 255, 0.14);
  --border: rgba(255, 255, 255, 0.12);
}

/* 6) 内嵌终端：强制暗色 */
body[data-dsh-arknights] [class*='terminal' i],
body[data-dsh-arknights] [class*='Terminal'],
body[data-dsh-arknights] .xterm,
body[data-dsh-arknights] .xterm-viewport,
body[data-dsh-arknights] .xterm-screen {
  background: #0a0b0d !important;
  color: #dce8ee !important;
}

body[data-dsh-arknights] .xterm .xterm-viewport {
  background: #0a0b0d !important;
}

/* 7) HUD 徽记：替换自带图标 */
body[data-dsh-arknights] [data-slot='sidebar'] button[class*='newSession'] svg {
  display: none !important;
}

body[data-dsh-arknights] [data-slot='sidebar'] button[class*='newSession']::before {
  content: '';
  display: inline-block;
  width: 15px;
  height: 15px;
  flex: none;
  background: url(__EMBLEM_CUBE__) center/contain no-repeat;
  filter: drop-shadow(0 0 4px rgba(53, 200, 245, 0.6));
  animation: ak-icon-pulse 3.5s ease-in-out infinite;
}

body[data-dsh-arknights] [data-slot='sidebar.brand.mark'] img,
body[data-dsh-arknights] [data-slot='sidebar.brand.mark'] svg {
  display: none !important;
}

body[data-dsh-arknights] [data-slot='sidebar.brand.mark'] {
  background: url(__EMBLEM_WING__) center/contain no-repeat !important;
  min-width: 26px;
  min-height: 26px;
  filter: drop-shadow(0 0 6px rgba(53, 200, 245, 0.45));
}

#ak-decor .ak-deco-core {
  position: absolute;
  top: 12%;
  left: 5%;
  width: 180px;
  height: 180px;
  background: url(__EMBLEM_CORE__) center/contain no-repeat;
  opacity: 0.5;
  filter: drop-shadow(0 0 24px rgba(53, 200, 245, 0.3));
  animation: ak-core-spin 90s linear infinite, ak-core-glow 6s ease-in-out infinite;
}

@keyframes ak-core-spin {
  to { transform: rotate(360deg); }
}

@keyframes ak-core-glow {
  0%, 100% { opacity: 0.38; }
  50% { opacity: 0.72; }
}

@keyframes ak-icon-pulse {
  0%, 100% { opacity: 0.75; filter: drop-shadow(0 0 2px rgba(53, 200, 245, 0.4)); }
  50% { opacity: 1; filter: drop-shadow(0 0 8px rgba(53, 200, 245, 0.9)); }
}

/* ── HUD 装饰层 ── */
#ak-decor {
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  overflow: hidden;
  font-family: ui-monospace, Consolas, monospace;
  animation: ak-fade-in 0.9s ease-out;
}

#ak-decor .ak-deco-bg {
  position: absolute;
  inset: 0;
  background:
    linear-gradient(rgba(5, 7, 10, 0.22), rgba(5, 7, 10, 0.34)),
    url('__AK_BG_URL__') center / cover no-repeat;
}

#ak-decor .ak-deco-cyanblock {
  position: absolute;
  top: 10%;
  left: 0;
  width: 26vw;
  height: 42vh;
  background: linear-gradient(120deg, rgba(53, 200, 245, 0.13), rgba(53, 200, 245, 0.03));
  clip-path: polygon(0 0, 100% 0, 74% 100%, 0 78%);
}

#ak-decor .ak-deco-grid {
  position: absolute;
  inset: 0;
  background-image: repeating-linear-gradient(45deg, rgba(255, 255, 255, 0.026) 0 1px, transparent 1px 52px);
}

#ak-decor .ak-deco-scan {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(0deg, rgba(255, 255, 255, 0.012) 0 2px, transparent 2px 4px);
}

#ak-decor .ak-deco-ghost {
  position: absolute;
  bottom: -3.2vw;
  left: -1.2vw;
  font-size: 15vw;
  font-weight: 900;
  letter-spacing: -0.02em;
  color: rgba(255, 255, 255, 0.1);
  white-space: nowrap;
  line-height: 0.82;
  animation: ak-ghost-breathe 9s ease-in-out infinite;
}

#ak-decor .ak-deco-meta {
  position: absolute;
  font-size: 10px;
  letter-spacing: 0.28em;
  color: rgba(255, 255, 255, 0.55);
  text-transform: uppercase;
}

#ak-decor .ak-deco-meta.tl { top: 14px; left: 18px; }
#ak-decor .ak-deco-meta.tr { top: 14px; right: 20px; }
#ak-decor .ak-deco-meta.bl { bottom: 12px; left: 18px; }

/* 背景层附加装饰字符：坐标 / 版本号 / 十字准星 */
#ak-decor .ak-deco-meta.coords {
  top: 30px;
  right: 20px;
  font-size: 8px;
  letter-spacing: 0.22em;
  color: rgba(255, 255, 255, 0.3);
}

#ak-decor .ak-deco-meta.b2 {
  bottom: 26px;
  left: 18px;
  font-size: 8px;
  letter-spacing: 0.22em;
  color: rgba(53, 200, 245, 0.34);
}

#ak-decor .ak-deco-cross {
  position: absolute;
  font-size: 15px;
  font-weight: 300;
  color: rgba(255, 255, 255, 0.13);
  user-select: none;
}

#ak-decor .ak-deco-cross.c1 { top: 31%; left: 58%; }
#ak-decor .ak-deco-cross.c2 { top: 67%; left: 37%; }
#ak-decor .ak-deco-cross.c3 { top: 21%; left: 81%; }

#ak-decor .ak-deco-count {
  position: absolute;
  right: 20px;
  bottom: 10px;
  display: flex;
  align-items: baseline;
  gap: 8px;
}

#ak-decor .ak-deco-count .num {
  font-size: 26px;
  font-weight: 700;
  color: #35c8f5;
}

#ak-decor .ak-deco-count .frac {
  font-size: 10px;
  color: rgba(255, 255, 255, 0.45);
}

#ak-decor .ak-deco-rail {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  width: 3px;
  background: linear-gradient(180deg, #35c8f5 0%, rgba(53, 200, 245, 0.1) 45%, #35c8f5 100%);
  background-size: 100% 300%;
  animation: ak-rail-flow 8s linear infinite;
}

#ak-decor .ak-deco-hazard {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: repeating-linear-gradient(-45deg, rgba(255, 217, 2, 0.85) 0 10px, rgba(10, 11, 13, 0.9) 10px 20px);
  background-size: 56px 3px;
  opacity: 0.45;
  animation: ak-hazard-scroll 26s linear infinite;
}

/* HUD 四角括号 */
#ak-decor .ak-deco-corner {
  position: absolute;
  width: 22px;
  height: 22px;
  border: 0 solid rgba(53, 200, 245, 0.7);
}

#ak-decor .ak-deco-corner.tl { top: 8px; left: 8px; border-top-width: 2px; border-left-width: 2px; }
#ak-decor .ak-deco-corner.tr { top: 8px; right: 8px; border-top-width: 2px; border-right-width: 2px; }
#ak-decor .ak-deco-corner.bl { bottom: 8px; left: 8px; border-bottom-width: 2px; border-left-width: 2px; }
#ak-decor .ak-deco-corner.br { bottom: 8px; right: 8px; border-bottom-width: 2px; border-right-width: 2px; }

#root, [id*='root'] {
  position: relative;
  z-index: 1;
}

/* ── 动效（全部 transform/opacity） ── */
@keyframes ak-scan-sweep {
  0% { transform: translateX(-30%); opacity: 0; }
  15% { opacity: 0.75; }
  85% { opacity: 0.75; }
  100% { transform: translateX(190%); opacity: 0; }
}

@keyframes ak-ghost-breathe {
  0%, 100% { opacity: 0.55; transform: scale(1); }
  50% { opacity: 1; transform: scale(1.018); }
}

@keyframes ak-rail-flow {
  0% { background-position: 0% 0; }
  100% { background-position: 0% 300%; }
}

@keyframes ak-hazard-scroll {
  to { background-position: 56px 0; }
}

@keyframes ak-fade-in {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* 呼吸系列：角标 / 青色块 / 核心徽章 */
@keyframes ak-corner-breathe {
  0%, 100% { opacity: 0.45; }
  50% { opacity: 1; }
}

@keyframes ak-cyanblock-breathe {
  0%, 100% { opacity: 0.5; transform: translateY(0); }
  50% { opacity: 1; transform: translateY(6px); }
}

#ak-decor .ak-deco-corner {
  animation: ak-corner-breathe 4.5s ease-in-out infinite;
}
#ak-decor .ak-deco-corner.tr { animation-delay: 1.1s; }
#ak-decor .ak-deco-corner.br { animation-delay: 2.2s; }
#ak-decor .ak-deco-corner.bl { animation-delay: 3.3s; }

#ak-decor .ak-deco-cyanblock {
  animation: ak-cyanblock-breathe 7s ease-in-out infinite;
}

/* HUD 装饰层 · 顶层（浮在界面之上：粒子 + 扫光） */
#ak-decor-top {
  position: fixed;
  inset: 0;
  z-index: 99999;
  pointer-events: none;
  overflow: hidden;
}

#ak-decor-top .ak-deco-sweep {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  width: 26%;
  background: linear-gradient(100deg, transparent, rgba(53, 200, 245, 0.045) 45%, rgba(53, 200, 245, 0.09) 50%, rgba(53, 200, 245, 0.045) 55%, transparent);
  transform: translateX(-30%);
  animation: ak-scan-sweep 9s ease-in-out infinite;
}

/* 顶层装饰字符：边缘竖排 + 十六进制码 + 刻度条 */
#ak-decor-top .ak-deco-vl,
#ak-decor-top .ak-deco-vr {
  position: absolute;
  top: 50%;
  writing-mode: vertical-rl;
  font-size: 9px;
  letter-spacing: 0.42em;
  text-transform: uppercase;
  white-space: nowrap;
  user-select: none;
}

#ak-decor-top .ak-deco-vl {
  left: 9px;
  transform: translateY(-50%);
  color: rgba(53, 200, 245, 0.38);
}

#ak-decor-top .ak-deco-vr {
  right: 9px;
  transform: translateY(-50%);
  color: rgba(255, 255, 255, 0.28);
}

#ak-decor-top .ak-deco-hex {
  position: absolute;
  top: 7px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 9px;
  letter-spacing: 0.24em;
  color: rgba(53, 200, 245, 0.42);
  user-select: none;
}

#ak-decor-top .ak-deco-ticks {
  position: absolute;
  bottom: 7px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 8px;
  letter-spacing: 7px;
  color: rgba(255, 255, 255, 0.26);
  user-select: none;
}

/* 侧栏装饰：TERRA 行 / R.I. 徽标水印 / 右缘刻度列 */
#ak-decor-top .ak-deco-terra {
  position: absolute;
  left: 16px;
  bottom: 5px;
  font-size: 8px;
  letter-spacing: 0.3em;
  color: rgba(244, 247, 249, 0.42);
  user-select: none;
}

#ak-decor-top .ak-deco-ri {
  position: absolute;
  top: 53%;
  left: 30px;
  width: 130px;
  user-select: none;
  pointer-events: none;
}

#ak-decor-top .ak-deco-ri img {
  width: 62px;
  height: 62px;
  object-fit: contain;
  opacity: 0.42;
  display: block;
  margin-left: 12px;
}

#ak-decor-top .ak-deco-ri span {
  display: block;
  margin-top: 10px;
  font-size: 9px;
  letter-spacing: 0.2em;
  line-height: 1.8;
  color: rgba(244, 247, 249, 0.52);
}

#ak-decor-top .ak-deco-vticks {
  position: absolute;
  right: 9px;
  top: 15%;
  width: 2px;
  height: 20vh;
  background: repeating-linear-gradient(180deg, rgba(53, 200, 245, 0.4) 0 5px, transparent 5px 11px);
}

/* 侧栏注入文字：logo 副标题 / 工作区英文 */
.ak-brand-sub {
  position: absolute;
  top: calc(100% + 6px);
  left: 6px;
  font-family: ui-monospace, Consolas, monospace;
  font-size: 8px;
  letter-spacing: 0.3em;
  white-space: nowrap;
  color: rgba(244, 247, 249, 0.42);
  user-select: none;
  pointer-events: none;
  z-index: 5;
}

.ak-ws-en {
  display: block;
  font-family: ui-monospace, Consolas, monospace;
  font-size: 8px;
  letter-spacing: 0.34em;
  color: rgba(53, 200, 245, 0.5);
  margin-top: 2px;
  user-select: none;
}

/* 粒子画布 */
#ak-decor-top canvas.ak-deco-particles {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

/* ── 原子模型图标：深度思考指示器 ── */
.ak-atom-icon {
  width: 1.1em;
  height: 1.1em;
  display: inline-block;
  vertical-align: -0.18em;
  flex-shrink: 0;
}

.ak-atom-icon .ak-orbit {
  transform-box: view-box;
  transform-origin: center;
  animation: ak-orbit-spin 2.6s linear infinite;
}

.ak-atom-icon .ak-orbit.o2 {
  animation-duration: 3.6s;
  animation-direction: reverse;
}

.ak-atom-icon .ak-orbit.o3 {
  animation-duration: 4.4s;
}

.ak-atom-icon .ak-nucleus {
  animation: ak-icon-pulse 2s ease-in-out infinite;
}

.ak-atom-icon .ak-electron {
  filter: drop-shadow(0 0 2.5px rgba(53, 200, 245, 0.9));
}

@keyframes ak-orbit-spin {
  to { transform: rotate(360deg); }
}

@media (prefers-reduced-motion: reduce) {
  #ak-decor, #ak-decor * {
    animation: none !important;
  }
}
"""

css_b64 = base64.b64encode(css.encode('utf-8')).decode('ascii')

client = """(() => {
  try {
    window.__ModuleLoader__.load({
      id: "@dsh-external/dsh-client-ui-skin-arknights",
      factory: (require) => {
        var module = { exports: {} };
        var exports = module.exports;
        Object.defineProperty(exports, Symbol.toStringTag, { value: "Module" });

        var inject = ["slots"];

        var THEME_CSS_B64 = "__CSS_B64__";
        var BG_B64 = "__BG_B64__";
        var EMBLEM_CORE_B64 = "__EMBLEM_CORE_B64__";

        function b64ToText(b64) {
          var bytes = Uint8Array.from(atob(b64), function (c) { return c.charCodeAt(0); });
          return new TextDecoder().decode(bytes);
        }

        function apply(ctx) {
          ctx.effect(function () {
            function injectTheme() {
              document.body.setAttribute("data-dsh-arknights", "");
              if (!document.getElementById("dsh-arknights-skin-style")) {
                var el = document.createElement("style");
                el.id = "dsh-arknights-skin-style";
                el.textContent = b64ToText(THEME_CSS_B64).split("__AK_BG_URL__").join("data:image/png;base64," + BG_B64);
                document.head.appendChild(el);
              }
              if (!document.getElementById("ak-decor")) {
                var decor = document.createElement("div");
                decor.id = "ak-decor";
                decor.innerHTML =
                  '<div class="ak-deco-bg"></div>' +
                  '<div class="ak-deco-cyanblock"></div>' +
                  '<div class="ak-deco-core"></div>' +
                  '<div class="ak-deco-grid"></div>' +
                  '<div class="ak-deco-scan"></div>' +
                  '<div class="ak-deco-ghost">ARKNIGHTS</div>' +
                  '<div class="ak-deco-rail"></div>' +
                  '<div class="ak-deco-hazard"></div>' +
                  '<div class="ak-deco-corner tl"></div>' +
                  '<div class="ak-deco-corner tr"></div>' +
                  '<div class="ak-deco-corner bl"></div>' +
                  '<div class="ak-deco-corner br"></div>' +
                  '<div class="ak-deco-meta tr">00 // 03 · WEBUI TERMINAL</div>' +
                  '<div class="ak-deco-meta bl">NEWAPI // GATEWAY</div>' +
                  '<div class="ak-deco-meta coords">GRID 04 · SEC.7 · 34.16N 108.85E</div>' +
                  '<div class="ak-deco-meta b2">VER 2.0.9 // BUILD 0941 · R.I. AUTH LEVEL 4</div>' +
                  '<div class="ak-deco-cross c1">+</div>' +
                  '<div class="ak-deco-cross c2">+</div>' +
                  '<div class="ak-deco-cross c3">+</div>' +
                  '<div class="ak-deco-count"><span class="num">00</span><span class="frac">// 03 INDEX</span></div>';
                document.body.appendChild(decor);
              }
              if (!document.getElementById("ak-decor-top")) {
                var top = document.createElement("div");
                top.id = "ak-decor-top";
                top.innerHTML =
                  '<canvas class="ak-deco-particles"></canvas>' +
                  '<div class="ak-deco-sweep"></div>' +
                  '<div class="ak-deco-vl">RHODES ISLAND OPERATIONS</div>' +
                  '<div class="ak-deco-vr">AUTHORIZED PERSONNEL ONLY ▮▮▯</div>' +
                  '<div class="ak-deco-vticks"></div>' +
                  '<div class="ak-deco-hex">0x0000 :: SYNC 0000</div>' +
                  '<div class="ak-deco-ticks">▮▮▯▮▮▮▯▮▮▯▮</div>' +
                  '<div class="ak-deco-terra">TERRA // A BRIGHTER TOMORROW</div>' +
                  '<div class="ak-deco-ri"><img src="data:image/png;base64,__EMBLEM_CORE_B64__" draggable="false" alt=""/><span>RHODES ISLAND<br/>FOR A BETTER TOMORROW</span></div>';
                document.body.appendChild(top);
              }
            }
            injectTheme();
            var observer = new MutationObserver(function () {
              if (!document.body.hasAttribute("data-dsh-arknights") || !document.getElementById("dsh-arknights-skin-style") || !document.getElementById("ak-decor") || !document.getElementById("ak-decor-top")) {
                injectTheme();
              }
            });
            observer.observe(document.body, { attributes: true, attributeFilter: ["data-dsh-arknights"] });
            observer.observe(document.head, { childList: true });

            /* ── 粒子系统：青色浮尘 + 闪烁光点，对标官网 hero ── */
            var rafId = 0;
            var particles = [];
            var reducedMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

            function startParticles() {
              var canvas = document.querySelector("#ak-decor-top canvas.ak-deco-particles");
              if (!canvas) return;
              var ctx = canvas.getContext("2d");
              if (!ctx) return;
              var dpr = Math.min(window.devicePixelRatio || 1, 2);
              var W = 0, H = 0;

              function resize() {
                W = canvas.clientWidth; H = canvas.clientHeight;
                canvas.width = Math.max(1, Math.round(W * dpr));
                canvas.height = Math.max(1, Math.round(H * dpr));
                ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
              }
              resize();
              window.addEventListener("resize", resize);

              var COUNT = 90;
              for (var i = 0; i < COUNT; i++) {
                particles.push({
                  x: Math.random(), y: Math.random(),
                  r: 0.7 + Math.random() * 1.6,
                  vy: 0.01 + Math.random() * 0.024,
                  vx: (Math.random() - 0.5) * 0.007,
                  a: 0.2 + Math.random() * 0.5,
                  tw: Math.random() * Math.PI * 2,
                  tws: 0.4 + Math.random() * 1.2
                });
              }

              var last = performance.now();
              function frame(now) {
                rafId = requestAnimationFrame(frame);
                var dt = Math.min((now - last) / 1000, 0.05);
                last = now;
                if (document.hidden) return;
                ctx.clearRect(0, 0, W, H);
                for (var i = 0; i < particles.length; i++) {
                  var p = particles[i];
                  p.y -= p.vy * dt;
                  p.x += p.vx * dt;
                  p.tw += p.tws * dt;
                  if (p.y < -0.02) { p.y = 1.02; p.x = Math.random(); }
                  if (p.x < -0.02) p.x = 1.02; else if (p.x > 1.02) p.x = -0.02;
                  var alpha = p.a * (0.55 + 0.45 * Math.sin(p.tw));
                  var px = p.x * W, py = p.y * H;
                  ctx.beginPath();
                  ctx.arc(px, py, p.r, 0, Math.PI * 2);
                  ctx.fillStyle = "rgba(53, 200, 245, " + alpha.toFixed(3) + ")";
                  ctx.fill();
                }
              }

              if (reducedMotion) {
                last = performance.now();
                ctx.clearRect(0, 0, W, H);
                for (var j = 0; j < particles.length; j++) {
                  var q = particles[j];
                  ctx.beginPath();
                  ctx.arc(q.x * W, q.y * H, q.r, 0, Math.PI * 2);
                  ctx.fillStyle = "rgba(53, 200, 245, " + (q.a * 0.6).toFixed(3) + ")";
                  ctx.fill();
                }
              } else {
                rafId = requestAnimationFrame(frame);
              }

              return function stopParticles() {
                cancelAnimationFrame(rafId);
                window.removeEventListener("resize", resize);
              };
            }

            var stopParticles = startParticles();

            /* ── 深度思考指示器 → 原子模型图标（电子沿轨道运动） ── */
            var ATOM_SVG =
              '<svg class="ak-atom-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">' +
              '<g class="ak-orbit" stroke="currentColor" stroke-width="1.1" opacity="0.85">' +
              '<ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(-28 12 12)"/>' +
              '<circle class="ak-electron" cx="20.8" cy="7.3" r="1.5" fill="#35c8f5" stroke="none"/>' +
              '</g>' +
              '<g class="ak-orbit o2" stroke="currentColor" stroke-width="1.1" opacity="0.85">' +
              '<ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(32 12 12)"/>' +
              '<circle class="ak-electron" cx="3.5" cy="6.7" r="1.5" fill="#7fdcff" stroke="none"/>' +
              '</g>' +
              '<g class="ak-orbit o3" stroke="currentColor" stroke-width="1.1" opacity="0.6">' +
              '<ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(90 12 12)"/>' +
              '<circle class="ak-electron" cx="12" cy="2" r="1.4" fill="#35c8f5" stroke="none"/>' +
              '</g>' +
              '<circle class="ak-nucleus" cx="12" cy="12" r="2.1" fill="currentColor"/>' +
              '</svg>';

            var THINK_RE = /(已)?深度思考|思考中|思考完成/;

            function makeAtomIcon() {
              var holder = document.createElement('span');
              holder.innerHTML = ATOM_SVG;
              return holder.firstChild;
            }

            function upgradeThinkIcons() {
              var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
                acceptNode: function (node) {
                  if (!node.parentElement) return NodeFilter.FILTER_REJECT;
                  if (node.parentElement.closest('#ak-decor,#ak-decor-top,script,style')) return NodeFilter.FILTER_REJECT;
                  var t = node.textContent || '';
                  return (t.length <= 24 && THINK_RE.test(t)) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
                }
              });
              var seen = new Set();
              while (walker.nextNode()) {
                var textEl = walker.currentNode.parentElement;
                if (seen.has(textEl)) continue;
                seen.add(textEl);
                var container = textEl.closest('button,[role="button"],[data-cordis-row],header,[class*="head"],[class*="title"]') || textEl.parentElement;
                if (!container || container.querySelector('.ak-atom-icon')) continue;
                var oldSvg = container.querySelector('svg');
                var atom = makeAtomIcon();
                if (oldSvg && oldSvg.parentElement === container) {
                  container.replaceChild(atom, oldSvg);
                } else {
                  textEl.parentElement.insertBefore(atom, textEl);
                }
              }
            }

            /* ── 浅色控件兜底：全局扫描写死白底的按钮/徽章 → 青色系 ── */
            function fixLightWidgets() {
              var els = document.querySelectorAll('button, [role="button"], span[class*="tag"], span[class*="badge"], span[class*="Tag"], span[class*="Badge"]');
              for (var i = 0; i < els.length; i++) {
                var el = els[i];
                if (el.dataset.akFixed) continue;
                if (el.closest('#ak-decor,#ak-decor-top')) continue;
                var r = el.getBoundingClientRect();
                if (r.width < 8 || r.width > 320 || r.height < 8 || r.height > 64) continue;
                var cs = window.getComputedStyle(el);
                var m = cs.backgroundColor.match(/rgba?\((\d+), (\d+), (\d+)(?:, ([\d.]+))?/);
                if (!m) continue;
                var R = +m[1], G = +m[2], B = +m[3], A = m[4] === undefined ? 1 : +m[4];
                if (R > 200 && G > 200 && B > 200 && A > 0.5) {
                  el.style.background = 'rgba(53, 200, 245, 0.14)';
                  el.style.border = '1px solid rgba(53, 200, 245, 0.45)';
                  el.style.color = '#7fdcff';
                  el.style.borderRadius = '2px';
                  el.dataset.akFixed = '1';
                }
              }
            }

            var thinkTimer = setInterval(function () {
              upgradeThinkIcons();
              upgradeHudTexts();
              fixLightWidgets();
            }, 900);
            setTimeout(function () { upgradeThinkIcons(); upgradeHudTexts(); fixLightWidgets(); }, 300);

            /* ── 侧栏双语装饰：logo 副标题 / 工作区·WORKSPACE ── */
            function upgradeHudTexts() {
              if (!document.querySelector('.ak-brand-sub')) {
                var sidebar = document.querySelector('[data-slot="sidebar"]');
                if (sidebar) {
                  var brandBtn = sidebar.querySelector('button[class*="brand"], [class*="brandName"]');
                  if (brandBtn) {
                    brandBtn.style.position = 'relative';
                    brandBtn.style.overflow = 'visible';
                    var sub = document.createElement('div');
                    sub.className = 'ak-brand-sub';
                    sub.textContent = 'RHODES ISLAND // COMPUTING CENTER';
                    brandBtn.appendChild(sub);
                  }
                }
              }
              if (!document.querySelector('.ak-ws-en')) {
                var ws = null;
                var all = document.querySelectorAll('[data-slot="sidebar"] span,[data-slot="sidebar"] div');
                for (var k = 0; k < all.length; k++) {
                  if (all[k].childElementCount === 0 && all[k].textContent.trim() === '工作区') { ws = all[k]; break; }
                }
                if (ws) {
                  var en = document.createElement('span');
                  en.className = 'ak-ws-en';
                  en.textContent = 'WORKSPACE';
                  ws.parentElement.insertBefore(en, ws.nextSibling);
                }
              }
            }

            /* ── 停止态扫描：生成中把发送徽章换成菱形停止徽章 ── */
            var stopTimer = setInterval(function () {
              var b = document.querySelector("[data-composer-card] button[class*='_primary']");
              if (!b) return;
              var svg = b.querySelector('svg');
              var isStop = !!(svg && svg.querySelector('rect')) || b.getAttribute('aria-label') === '停止生成';
              if (isStop && !b.hasAttribute('data-ak-stop')) {
                b.setAttribute('data-ak-stop', '');
              } else if (!isStop && b.hasAttribute('data-ak-stop')) {
                b.removeAttribute('data-ak-stop');
              }
            }, 250);

            /* ── 十六进制读数滚动（HUD 数据流） ── */
            var hexTimer = 0;
            if (!reducedMotion) {
              var HEXC = "0123456789ABCDEF";
              hexTimer = setInterval(function () {
                var el = document.querySelector("#ak-decor-top .ak-deco-hex");
                if (!el) return;
                var s = "0x";
                for (var i = 0; i < 4; i++) s += HEXC[(Math.random() * 16) | 0];
                s += " :: SYNC ";
                for (var j = 0; j < 4; j++) s += HEXC[(Math.random() * 16) | 0];
                el.textContent = s;
              }, 160);
            }

            return function () {
              observer.disconnect();
              if (stopParticles) stopParticles();
              clearInterval(thinkTimer);
              clearInterval(stopTimer);
              clearInterval(hexTimer);
              Array.prototype.forEach.call(document.querySelectorAll('.ak-atom-icon'), function (n) { n.remove(); });
              var el = document.getElementById("dsh-arknights-skin-style");
              if (el) el.remove();
              var decor = document.getElementById("ak-decor");
              if (decor) decor.remove();
              var decorTop = document.getElementById("ak-decor-top");
              if (decorTop) decorTop.remove();
              document.body.removeAttribute("data-dsh-arknights");
            };
          });
        }

        exports.name = "dsh-arknights-theme";
        exports.inject = inject;
        exports.apply = apply;
        return module.exports;
      }
    });
  } catch (err) {
    console.warn('[AI Client Sandbox] dsh-arknights-theme runtime error:', err);
  }
})();
"""

css_full = css.replace('__EMBLEM_CORE__', em_core).replace('__EMBLEM_WING__', em_wing).replace('__EMBLEM_CUBE__', em_cube).replace('__EMBLEM_SEND__', em_send).replace('__EMBLEM_STOP__', em_stop)
css_b64 = base64.b64encode(css_full.encode('utf-8')).decode('ascii')

client = client.replace('__CSS_B64__', css_b64).replace('__BG_B64__', bg_b64).replace('__EMBLEM_CORE_B64__', em_core.split(',', 1)[1])
open('lib/client.js', 'w', encoding='utf-8', newline='\n').write(client)

css_pub = css.replace('__AK_BG_URL__', './assets/ak-sub-bg.png').replace('__EMBLEM_CORE__', './assets/ak-emblem-core.png').replace('__EMBLEM_WING__', './assets/ak-emblem-wing.png').replace('__EMBLEM_CUBE__', './assets/ak-emblem-cube.png').replace('__EMBLEM_SEND__', './assets/ak-emblem-send.png').replace('__EMBLEM_STOP__', './assets/ak-emblem-stop.png')
open('assets/theme-preview.css', 'w', encoding='utf-8', newline='\n').write(css_pub)

print('FINAL client.js written, size =', len(client))
