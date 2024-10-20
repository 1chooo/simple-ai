import Home from "@/src/components/home";
import Sponsors from "@/src/components/sponsors";
import Leaders from "@/src/components/leaders";
import Newsletter from "@/src/components/newsletter";
import Head from "next/head";

export default function Index() {
  return (
    <>
      <Head>
        <title>LinkScape | Home</title>
      </Head>
      <Home />
      <Sponsors />
      <Leaders />
      <Newsletter />
    </>
  );
}
