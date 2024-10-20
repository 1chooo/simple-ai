/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    domains: [
      "cdn.linkscape.app",
      "avatars.githubusercontent.com",
      "files.ohevan.com",
    ],
  },
};

module.exports = nextConfig;
