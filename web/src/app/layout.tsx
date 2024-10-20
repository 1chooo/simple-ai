import "./globals.css";
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import { Analytics } from "@vercel/analytics/react";
import Footer from "@/src/components/footer";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Refinaid",
  description: "We are a group of student hackers",
  icons: {
    shortcut: "/favicon.png",
  },
  openGraph: {
    title: "Refinaid",
    description: "We are Refinaid.",
    url: "https://linkscape.app",
    siteName: "Refinaid",
    images: [
      {
        url: "https://cdn.linkscape.app/linkscape-logo.png",
        width: 2608,
        height: 769,
      },
    ],
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <div
          className={
            "background-dotted w-screen fixed left-0 top-0 h-screen z-[-1] dark:opacity-10"
          }
        />
        {children}

        <Analytics />
        <Footer />
      </body>
    </html>
  );
}
