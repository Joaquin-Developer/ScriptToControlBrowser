const {Builder} = require('selenium-webdriver');

(async function myFunction() {
    let driver = await new Builder().forBrowser('chromium').build();
    //your code inside this block
})();
