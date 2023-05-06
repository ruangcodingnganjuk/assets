const { Telegraf } = require("telegraf");
const bot = new Telegraf("5887781535:AAF8AXMDMtfAjjrr0zEaShztySq-vw6utno");
// const bot = process.env.TELEGRAM_BOT_TOKEN

bot.command("start", (ctx) => {
  console.log(ctx.from);
  bot.telegram.sendMessage(
    ctx.chat.id,
    "haloo!! Selamat datang di RCN_bot",
    {}
  );
});

bot.command("help", (ctx) => {
  console.log(ctx.from);
  bot.telegram.sendMessage(
    ctx.chat.id,
    "Butuh bantuan",
    {}
  );
});

bot.launch();
