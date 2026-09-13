// dsh-arknights-theme — 服务端半区（极简）：主题为纯客户端外观注入。
export const name = "dsh-arknights-theme";
export const inject = [];

export function apply(ctx) {
  ctx.effect(() => {
    ctx.logger?.info?.("[dsh-arknights-theme] 明日方舟主题已加载（纯外观注入，零提示词干预）");
  });
}
