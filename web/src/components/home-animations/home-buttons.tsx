"use client";
import Link from "next/link";
import { HeartIcon, MarkGithubIcon } from "@primer/octicons-react";
import { motion } from "framer-motion";

const containerVariants = {
  initial: {
    opacity: 0,
    y: 50,
  },
  animate: {
    opacity: 1,
    y: 0,
    transition: {
      type: "spring",
      stiffness: 100,
      damping: 20,
      delay: 1.3,
    },
  },
};

export default function HomeButtons() {
  const button1delay = 1.3;
  const button2delay = 1.45;

  return (
    <motion.div
      variants={containerVariants}
      initial="initial"
      animate="animate"
      className="mt-10 flex flex-row gap-3"
    >
      <motion.div
        initial={{ opacity: 0, y: 50 }}
        animate={{
          opacity: 1,
          y: 0,
          transition: {
            type: "spring",
            stiffness: 100,
            damping: 20,
            delay: button1delay,
          },
        }}
      >
        <Link href={"https://github.com/LinkScapeOfficial"}>
          <button className="mr-3 flex items-center rounded-xl bg-gh-dark-bg px-6 py-3 gh-border text-white hover:bg-gh-gray-8 shadow-xl hover:shadow-2xl transition-all hover:scale-105 active:scale-95 active:shadow-sm">
            <MarkGithubIcon className="mr-2 h-5 w-5" />
            <div className="font-semibold">GitHub</div>
          </button>
        </Link>
      </motion.div>
      <motion.div
        initial={{ opacity: 0, y: 50 }}
        animate={{
          opacity: 1,
          y: 0,
          transition: {
            type: "spring",
            stiffness: 100,
            damping: 20,
            delay: button2delay,
          },
        }}
      >
        <Link href={"/donate"}>
          <button className="flex items-center rounded-xl bg-gh-bg px-4 py-3 gh-border text-gh-text-primary hover:bg-gradient-to-br hover:from-red-500/80 hover:to-pink-600/80 hover:text-white transition-all shadow-sm active:scale-95">
            <HeartIcon className="mr-2 h-5 w-5" />
            <div className="font-semibold">Donate</div>
          </button>
        </Link>
      </motion.div>
    </motion.div>
  );
}
