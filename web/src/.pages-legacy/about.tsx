import Link from "next/link";
import Head from "next/head";

export default function About() {
  return (
    <>
      <Head>
        <title>LinkScape | About</title>
      </Head>
      <div className="mb-20 mt-12 flex flex-col items-center justify-center sm:mb-64 sm:mt-60">
        <div
          className="absolute inset-0 grid grid-cols-2 -space-x-12 opacity-40 dark:opacity-20 sm:-space-x-52"
          style={{ zIndex: -1 }}
        >
          <div className="fix-safari-blur h-32 bg-gradient-to-br from-blue-500 to-blue-400 blur-[32px] dark:from-blue-700 sm:h-64 sm:blur-[106px]"></div>
          <div className="fix-safari-blur h-20 bg-gradient-to-r from-blue-400 to-blue-300 blur-[32px] dark:to-blue-600 sm:h-40 sm:blur-[106px]"></div>
        </div>
        <h1 className="text-center text-4xl font-bold sm:text-8xl">
          We{" "}
          <span className="bg-gradient-to-r from-blue-500 to-purple-700 bg-clip-text text-transparent">
            Hack,{" "}
          </span>
          We{" "}
          <span className="bg-gradient-to-r from-blue-500 to-purple-700 bg-clip-text text-transparent">
            Grow.
          </span>
        </h1>
        <p className="py-6 text-center text-base sm:text-lg">
          LinkScape is led by passionate students dedicated to influence the
          world through technology.
        </p>
        <h2 className="mb-8 mt-8 text-center text-2xl font-bold sm:text-4xl">
          Legal Documents
        </h2>
        <div className="flex flex-wrap">
          <Link
            href="https://cdn.linkscape.app/IRS_Letter.pdf"
            className="mr-6 transition-transform duration-300 hover:-translate-y-1"
          >
            <div className="max-w-sm rounded-lg border border-gray-200 bg-white shadow-md">
              <div className="flex items-center justify-center">
                <img
                  className="max-h-72 rounded-t-lg"
                  src="https://cdn.linkscape.app/IRS_Letter.png"
                  alt=""
                />
              </div>
              <div className="-mb-2 -mt-7 w-52 p-5 font-bold">
                IRS 501(c)(3) Status Determination Letter
              </div>
            </div>
          </Link>
          <Link
            href="https://cdn.linkscape.app/Certificate_of_Status.pdf"
            className="mr-6 transition-transform duration-300 hover:-translate-y-1"
          >
            <div className="h-100 max-w-sm rounded-lg border border-gray-200 bg-white shadow-md">
              <div className="flex items-center justify-center">
                <img
                  className="max-h-72 rounded-t-lg"
                  src="https://cdn.linkscape.app/Certificate_of_Status.png"
                  alt=""
                />
              </div>
              <div className="-mt-7 mb-4 w-52 p-5 font-bold">
                Certificate of Status
              </div>
            </div>
          </Link>
          <Link
            href="https://cdn.linkscape.app/fiscal_sponsorship_letter.pdf"
            className="mr-6 transition-transform duration-300 hover:-translate-y-1"
          >
            <div className="h-100 max-w-sm rounded-lg border border-gray-200 bg-white shadow-md">
              <div className="flex items-center justify-center">
                <img
                  className="max-h-72 rounded-t-lg"
                  src="https://cdn.linkscape.app/fiscal_sponsorship_letter.png"
                  alt=""
                />
              </div>
              <div className="-mb-2 -mt-7 w-52 p-5 font-bold">
                Fiscal Sponsorship Confirmation
              </div>
            </div>
          </Link>
        </div>
      </div>
    </>
  );
}
