import Image from "next/image";
import Link from "next/link";

export default function Sponsors() {
  return (
    <div className="bg-white py-24 sm:py-32">
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <h2 className="text-center text-xs font-semibold tracking-wide sm:text-lg text-gh-text-secondary">
          PROUDLY SPONSORED BY
        </h2>
        <div className="mx-auto mt-10 grid max-w-lg grid-cols-4 items-center gap-x-8 gap-y-10 sm:max-w-xl sm:grid-cols-6 sm:gap-x-10 lg:mx-0 lg:max-w-none lg:grid-cols-4">
          <Link
            href={"https://vercel.com/?utm_source=linkscape&utm_campaign=oss"}
          >
            <Image
              className="col-span-2 max-h-12 w-full object-contain lg:col-span-1"
              src="https://files.ohevan.com/tmp/Vercel_logo_black.svg"
              alt="Vercel"
              width={158}
              height={48}
            />
          </Link>
          <Link href={"https://www.figma.com/"}>
            <Image
              className="max-h-12 col-span-2 w-full object-contain lg:col-span-1"
              src="https://files.ohevan.com/tmp/Figma-Wordmark-Black.svg"
              alt="Figma"
              width={158}
              height={48}
            />
          </Link>
          <Link href={"https://1password.com"}>
            <Image
              className="col-span-2 max-h-12 w-full object-contain lg:col-span-1"
              src="https://files.ohevan.com/tmp/1password-logo.svg"
              alt="1Password"
              width={158}
              height={48}
            />
          </Link>
          <Link href={"https://www.twilio.com/"}>
            <Image
              className="col-span-2 max-h-12 w-full object-contain sm:col-start-2 lg:col-span-1"
              src="https://files.ohevan.com/tmp/Twilio-logo-red.svg"
              alt="Twilio"
              width={158}
              height={48}
            />
          </Link>
        </div>
      </div>
    </div>
  );
}
