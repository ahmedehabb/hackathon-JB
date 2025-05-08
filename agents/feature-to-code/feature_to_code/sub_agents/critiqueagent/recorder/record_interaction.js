const { chromium } = require('playwright');

(async () => {
  // console.log('Launching Chromium...');

    browser = await chromium.launch({
      headless: false,
      args: ['--start-maximized'],
    });
    // console.log('Chromium launched successfully.');


  let context, page;
  context = await browser.newContext({
    viewport: null,
    screen: { width: 1920, height: 1080 },
  });

  page = await context.newPage();


  await page.goto('http://localhost:3000');
  // console.log('✅ Navigated to http://localhost:3000');

  await page.evaluate(() => {
    document.body.requestFullscreen().catch(() => {
      // console.log('⚠️ Unable to use fullscreen mode programmatically!');
    });
  });

  await page.waitForTimeout(10000);

  await browser.close();
})();
