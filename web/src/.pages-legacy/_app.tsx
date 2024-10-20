import "@/src/app/globals.css";
import type { AppProps } from "next/app";
import Footer from "@/src/components/footer";
import Head from "next/head";
import { Analytics } from "@vercel/analytics/react";

export default function App({ Component, pageProps }: AppProps) {
  return (
    <>
      <Head>
        <meta
          name="description"
          content="We are a group of student hackers"
          key="desc"
        />
        <meta property="og:title" content="LinkScape" />
        <meta property="og:description" content="We are Linkscape." />
        <meta
          property="og:image"
          content="https://cdn.linkscape.app/linkscape-logo.png"
        />
      </Head>

      <Component {...pageProps} />
      <Analytics />
      <Footer />
    </>
  );
}
