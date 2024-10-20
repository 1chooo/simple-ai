export default function Hero() {
  return (
    <>
      <div className="absolute inset-0 grid grid-cols-2 -space-x-12 opacity-40 dark:opacity-20 sm:-space-x-52 z-[-1]">
        <div className="fix-safari-blur h-32 bg-gradient-to-br from-blue-500 to-blue-400 blur-[32px] dark:from-blue-700 sm:h-64 sm:blur-[106px]"></div>
        <div className="fix-safari-blur h-20 bg-gradient-to-r from-blue-400 to-blue-300 blur-[32px] dark:to-blue-600 sm:h-40 sm:blur-[106px]"></div>
      </div>
      <h1 className="text-center text-4xl font-bold sm:text-8xl sm:mt-52">
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
        LinkScape is led by passionate students dedicated to influencing the
        world through technology.
      </p>
    </>
  );
}
