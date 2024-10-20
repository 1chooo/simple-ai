"use client";
import { motion } from "framer-motion";
import { useEffect, useState } from "react";

const containerVariants = {
  initial: {
    opacity: 0,
    y: 50,
  },
  animate: {
    opacity: 1,
    y: 0,
    transition: {
      y: {
        type: "spring",
        stiffness: 100,
        damping: 20,
        delay: 1.3,
      },
    },
  },
};

const h1Variants = {
  initial: { opacity: 0, y: 20 },
  animate: {
    opacity: 1,
    y: 0,
    transition: {
      type: "spring",
      stiffness: 400,
      damping: 20,
    },
  },
};

const h2Variants = {
  initial: { opacity: 0, y: -20 },
  animate: {
    opacity: 1,
    y: 0,
    transition: {
      type: "spring",
      stiffness: 400,
      damping: 20,
      delay: 0.7,
    },
  },
};

const nameVariants = {
  initial: {
    opacity: 0,
    x: -40,
  },
  animate: {
    opacity: 1,
    x: 0,
    transition: {
      type: "spring",
      stiffness: 400,
      damping: 20,
      delay: 0.4,
    },
  },
};

export default function HomeTitle() {
  function BlinkingCursor() {
    const [isVisible, setIsVisible] = useState(true);

    useEffect(() => {
      const interval = setInterval(() => {
        setIsVisible((v) => !v);
      }, 533);

      return () => clearInterval(interval);
    }, []);

    return isVisible ? (
      <div className={"inline-block text-purple-700"}>_</div>
    ) : (
      <div className={"inline-block invisible"}>_</div>
    );
  }

  return (
    <motion.div
      variants={containerVariants}
      initial="initial"
      animate="animate"
      className="flex flex-col items-center justify-center w-full h-full z-3"
    >
      <motion.h1
        variants={h1Variants}
        initial="initial"
        animate="animate"
        className="text-center text-4xl font-bold sm:text-8xl"
      >
        We are{" "}
        <motion.span
          variants={nameVariants}
          initial="initial"
          animate="animate"
          className="block text-6xl sm:text-8xl sm:inline-block bg-gradient-to-r from-blue-500 to-purple-700 bg-clip-text text-transparent"
        >
          Refinaid
          <BlinkingCursor />
        </motion.span>
      </motion.h1>
      <motion.h2
        variants={h2Variants}
        initial="initial"
        animate="animate"
        className="px-4 py-6 text-center text-base sm:text-lg text-gh-text-secondary"
      >
        A group of students who hack, build, and compete together.
      </motion.h2>
    </motion.div>
  );
}
