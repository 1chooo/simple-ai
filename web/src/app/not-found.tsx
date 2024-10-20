import { FaDonate, FaHome } from "react-icons/fa";
import Link from "next/link";
import { Metadata } from "next";
import Header from "@/src/components/header";

export const metadata: Metadata = {
  title: "Refinaid | 404",
  description: "We are Refinaid.",
};

export default function Home() {
  return (
    <>
      <Header />
      <div className="mb-64 mt-60 flex flex-col items-center justify-center sm:mt-64">
        <div
          className="absolute inset-0 grid grid-cols-2 -space-x-12 opacity-40 dark:opacity-20 sm:-space-x-52"
          style={{ zIndex: -1 }}
        >
          <div className="fix-safari-blur h-32 bg-gradient-to-br from-blue-500 to-blue-400 blur-[32px] dark:from-blue-700 sm:h-64 sm:blur-[106px]"></div>
          <div className="fix-safari-blur h-20 bg-gradient-to-r from-blue-400 to-blue-300 blur-[32px] dark:to-blue-600 sm:h-40 sm:blur-[106px]"></div>
        </div>
        <h1 className="text-center text-4xl font-bold sm:text-8xl">
          <span className="bg-gradient-to-r from-blue-500 to-purple-700 bg-clip-text text-transparent">
            404 Error
          </span>
        </h1>
        <div className="py-6 text-center text-base sm:text-lg">
          Sorry, we couldn&apos;t find the page you&apos;re looking for.
          <br />
          But you can find us happy by donating to us!
        </div>
        <div className="flex flex-row">
          <Link href="/">
            <button className="mr-3 flex items-center rounded-md bg-black px-3 py-2 text-white">
              <FaHome className="mr-1.5 h-7 w-7" />
              <div className="font-semibold">Home</div>
            </button>
          </Link>
          <Link href="/">
            <button className="mr-3 flex items-center rounded-md bg-black px-3 py-2 text-white">
              <FaDonate className="mr-1.5 h-7 w-7" />
              <div className="font-semibold">Donate</div>
            </button>
          </Link>
        </div>
      </div>
    </>
  );
}
