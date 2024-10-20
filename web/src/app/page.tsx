import Leaders from "@/src/components/leaders";
import Newsletter from "@/src/components/newsletter";
import NavBar from "@/src/components/header";
import { Metadata } from "next";
import Sponsors from "@/src/components/sponsors";
import HomeTitle from "@/src/components/home-animations/home-title";
import HomeButtons from "@/src/components/home-animations/home-buttons";

export const metadata: Metadata = {
  title: "Refinaid | Home",
  description: "We are Refinaid.",
};

export default function Index() {
  return (
    <>
      <NavBar />
      <div
        className="absolute inset-0 grid grid-cols-2 -space-x-12 opacity-40 dark:opacity-20 sm:-space-x-52"
        style={{ zIndex: -1 }}
      >
        <div className="fix-safari-blur h-32 bg-gradient-to-br from-blue-500 to-blue-400 blur-[32px] dark:from-blue-700 sm:h-64 sm:blur-[106px]"></div>
        <div className="fix-safari-blur h-20 bg-gradient-to-r from-blue-400 to-blue-300 blur-[32px] dark:to-blue-600 sm:h-40 sm:blur-[106px]"></div>
      </div>
      <div className="mt-6 flex flex-col items-center justify-center min-h-screen">
        <HomeTitle />
        <HomeButtons />
      </div>
      <div className={"min-h-screen flex flex-col justify-center"}>
        <Leaders />
        <Newsletter />
      </div>

      <Sponsors />
    </>
  );
}
