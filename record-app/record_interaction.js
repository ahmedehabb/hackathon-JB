const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    headless: false,
    args: ['--start-maximized'],  // Maximize the browser window
  });

  const context = await browser.newContext({
    viewport: null, // Let the browser determine the full screen size
    screen: { width: 1920, height: 1080 }, // Match your display resolution (change as needed)
  });

  const page = await context.newPage();

  // Simulate F11 key press to enforce fullscreen mode
  await page.evaluate(() => {
    document.body.requestFullscreen().catch(() => {
      console.log('Unable to use fullscreen mode programmatically!');
    });
  });

  await page.goto('http://localhost:3000');

  // Wait for your app to load
  await page.waitForTimeout(5000);

  await browser.close();
})();