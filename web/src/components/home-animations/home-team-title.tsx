"use client";
import { motion, useInView, useAnimation, Variants } from "framer-motion";
import { useEffect, useRef } from "react";

export default function HomeTeamTitle({
  delay,
  children,
  className,
}: {
  delay: number;
  children: React.ReactNode;
  className?: string;
}) {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true });
  const controls = useAnimation();
  useEffect(() => {
    if (isInView) {
      controls.start("visible");
    }
  }, [controls, isInView]);

  let titleVariants: Variants = {
    initial: { opacity: 0, y: 40 },
    visible: {
      opacity: 1,
      y: 0,
      transition: {
        type: "spring",
        stiffness: 260,
        damping: 17,
        delay: delay ?? 0,
      },
    },
    exit: { opacity: 0, y: 40 },
  };

  return (
    <motion.h2
      ref={ref}
      variants={titleVariants}
      initial="initial"
      animate={controls}
      exit="exit"
      className={className}
    >
      {children}
    </motion.h2>
  );
}
