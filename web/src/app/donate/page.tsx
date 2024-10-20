import React from "react";
import NavBar from "@/src/components/header";
import { Metadata } from "next";

export const metadata: Metadata = {
  title: "LinkScape | Donate",
  description: "Donate to LinkScape",
};

export default function Donate() {
  return (
    <>
      <NavBar />
      <div className="h-512px screen flex flex-col mt-16">
        <iframe
          src="https://bank.hackclub.com/donations/start/linkscape"
          name="donateFrame"
          height="780px"
          width="screen"
          allowFullScreen
        ></iframe>
      </div>
    </>
  );
}
