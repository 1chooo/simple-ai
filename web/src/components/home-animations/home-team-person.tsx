"use client";
import { motion, useInView, useAnimation, Variants } from "framer-motion";
import { useEffect, useRef } from "react";
import Image from "next/image";
import Link from "next/link";

export default function HomeTeamPerson({
  delay,
  person,
}: {
  delay: number;
  person: {
    name: string;
    imageUrl: string;
    role: string;
    github: string;
  };
}) {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true });
  const controls = useAnimation();
  useEffect(() => {
    if (isInView) {
      controls.start("visible");
    }
  }, [controls, isInView]);

  let personVariants: Variants = {
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
    <motion.div
      ref={ref}
      variants={personVariants}
      initial="initial"
      animate={controls}
      exit="exit"
      className="flex items-center flex-col gap-y-3"
    >
      <Image
        className="h-28 w-28 rounded-full shadow-sm hover:shadow-lg transition-shadow duration-200 gh-border cursor-pointer"
        src={person.imageUrl}
        width={512}
        height={512}
        alt=""
      />
      <div className={"mt-1"}>
        <Link href={person.github}>
          <h3 className="text-lg font-semibold hover:underline leading-7 tracking-tight text-gray-900 text-center">
            {person.name}
          </h3>
        </Link>
        <p className="text-sm font-semibold leading-6 text-indigo-600 text-center w-40">
          {person.role}
        </p>
      </div>
    </motion.div>
  );
}
