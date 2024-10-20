import Link from "next/link";
import Image from "next/image";

const navigation = [
  { name: "About", href: "/about" },
  { name: "Team", href: "/team" },
  { name: "Projects", href: "/projects" },
];

const social = [
  {
    name: "GitHub",
    href: "https://github.com/refinaid",
  },
  {
    name: "Twitter",
    href: "https://twitter.com/RealLinkScape",
  },
  {
    name: "Discord",
    href: "https://discord.gg/WDdvabyKaH",
  },
];

export default function Footer() {
  return (
    <footer className="bg-gh-bg text-center text-black border-t border-gh-border py-12 px-4 sm:px-12 md:px-32">
      <section className="flex flex-col gap-6 sm:gap-0 sm:grid sm:grid-cols-12">
        <div className={"px-6 flex flex-col items-start sm:col-span-8"}>
          <Image
            src={
              "https://evan.beee.top/img/38a40a6e7aef11dee616fc3373c0f1d1-72dad.svg"
            }
            alt={"Linkscape logo"}
            width={648}
            height={2194}
            className={"w-56"}
          />
          <div className="text-base text-left text-gh-text-secondary  mt-6">
            © 2024 Refinaid. All rights reserved.{" "}
            <span className="inline">
              Deployed on
              <Link
                href={
                  "https://vercel.com/?utm_source=linkscape&utm_campaign=oss"
                }
              >
                <Image
                  src={"https://files.ohevan.com/tmp/Vercel_logo_black.svg"}
                  alt={"Vercel logo"}
                  width={158}
                  height={48}
                  className={"inline-block ml-2 w-20 "}
                />
              </Link>
            </span>
          </div>
        </div>

        <div className="hidden sm:flex flex-col justify-center items-start sm:col-start-9 md:col-start-10 px-6 sm:px-0">
          <h3 className="text-sm font-semibold text-gh-text-secondary">
            Contacts
          </h3>
          <div
            className={
              "flex flex-col mt-1 sm:mt-3 gap-0 sm:gap-0.5 items-start "
            }
          >
            {social.map((item) => (
              <Link
                href={item.href}
                key={item.name}
                className={"font-semibold text-base hover:underline"}
              >
                {item.name}
              </Link>
            ))}
          </div>
        </div>
        <div className="hidden sm:flex flex-col justify-center items-start sm:col-start-11  md:col-start-12 px-6 sm:px-0">
          <h3 className="text-sm font-semibold text-gh-text-secondary">
            Navigation
          </h3>
          <div
            className={
              "flex flex-col mt-1 sm:mt-3 gap-0 sm:gap-0.5 items-start "
            }
          >
            {navigation.map((item) => (
              <Link
                href={item.href}
                key={item.name}
                className={"font-semibold text-base hover:underline"}
              >
                {item.name}
              </Link>
            ))}
          </div>
        </div>
      </section>
    </footer>
  );
}
