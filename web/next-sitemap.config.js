/** @type {import('next-sitemap').IConfig} */
module.exports = {
  siteUrl: process.env.SITE_URL || "https://linkscape.app",
  generateRobotsTxt: true, // (optional)
  // ...other options
};
