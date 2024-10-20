import Link from "next/link";
import Head from "next/head";
import Image from "next/image";

const people = [
  {
    name: "Thomas Wu",
    role: "Founder & CEO",
    imageUrl: "https://cdn.linkscape.app/ThomasWu.png",
    github: "https://github.com/thomaswcy",
  },
  {
    name: "Meli Liu",
    role: "Founder",
    imageUrl: "https://cdn.linkscape.app/MeliLiu.png",
    github: "https://github.com/MeliLXT",
  },
  {
    name: "Jett Chen",
    role: "Co-Founder & CTO",
    imageUrl: "https://cdn.linkscape.app/JettChen.png",
    github: "https://github.com/JettChenT",
  },
  {
    name: "Snapdragon Lee",
    role: "Co-Founder",
    imageUrl: "https://avatars.githubusercontent.com/u/61799448",
    github: "https://github.com/SnapdragonLee",
  },
  {
    name: "Anthony Ji",
    role: "Co-Founder & Head of Singapore",
    imageUrl: "https://cdn.linkscape.app/AnthonyJi.jpg",
    github: "",
  },
  {
    name: "Andy Chang",
    role: "Senior Member",
    imageUrl: "https://cdn.linkscape.app/AndyChang.png",
    github: "https://github.com/xiaobaizzh",
  },
  {
    name: "Kai Xu",
    role: "Senior Member",
    imageUrl: "https://cdn.linkscape.app/KaiXu.png",
    github: "",
  },
  {
    name: "Tim Yu",
    role: "Senior Member",
    imageUrl: "",
    github: "",
  },
  {
    name: "Evoker Ma",
    role: "Senior Member",
    imageUrl: "https://cdn.linkscape.app/EvokerMa.png",
    github: "",
  },
  {
    name: "Kevin Zhang",
    role: "Senior Member",
    imageUrl: "https://cdn.linkscape.app/KevinZhang.png",
    github: "https://github.com/juicyk-cn",
  },
  {
    name: "Tze-Yun Hsiao",
    role: "Senior Member & Head of Design",
    imageUrl: "https://cdn.linkscape.app/TzeYunHsiao.png",
    github: "https://github.com/Powerlean",
  },
  {
    name: "Yucheng Zou",
    role: "Senior Member",
    imageUrl: "",
    github: "",
  },
  {
    name: "Nash Sun",
    role: "Senior Member",
    imageUrl: "https://cdn.linkscape.app/NashSun.png",
    github: "https://github.com/sun-xx",
  },
  {
    name: "Thedust Ye",
    role: "Senior Member",
    imageUrl: "https://cdn.linkscape.app/Thedustye.png",
    github: "https://github.com/Thedustye",
  },
  {
    name: "Patirck Peng",
    role: "Senior Member",
    imageUrl: "",
    github: "https://github.com/DDizzzy79",
  },
  {
    name: "Ana Jiang",
    role: "Senior Member",
    imageUrl: "https://cdn.linkscape.app/AnaJiang.jpg",
    github: "https://github.com/ana-jiangR",
  },
  {
    name: "Layla Ma",
    role: "Member",
    imageUrl: "",
    github: "https://github.com/Marion-China",
  },
  {
    name: "Eason Ji",
    role: "Member",
    imageUrl: "",
    github: "",
  },
  {
    name: "Newton Ngau",
    role: "Member",
    imageUrl: "",
    github: "",
  },
  {
    name: "Arnold Chao",
    role: "Member",
    imageUrl: "https://cdn.linkscape.app/ArnoldChao.png",
    github: "https://github.com/benxxxzzz",
  },
  {
    name: "Jaden Hou",
    role: "Member",
    imageUrl: "https://cdn.linkscape.app/JadenHou.png",
    github: "https://github.com/InternetRamen",
  },
  {
    name: "Otto Chou",
    role: "Member",
    imageUrl: "",
    github: "https://github.com/ottochou1",
  },
];

export default function Team() {
  return (
    <div className="mb-10 mt-5 bg-white">
      <Head>
        <title>LinkScape | Team</title>
      </Head>
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <h2 className="mt-12 text-center text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
          Meet Our Team
        </h2>
        <ul
          role="list"
          className="mt-8 grid gap-x-8 gap-y-6 sm:grid-cols-2 sm:gap-x-6 sm:gap-y-8 xl:grid-cols-3 xl:gap-y-10"
        >
          {people.map((person, index) => (
            <div key={index}>
              <li className="flex items-center justify-center">
                <div className="flex flex-col items-center gap-2">
                  <Image
                    className="h-16 w-16 rounded-full"
                    src={person.imageUrl}
                    width={512}
                    height={512}
                    alt=""
                  />
                  <div className="text-center">
                    <Link href={person.github}>
                      <h3 className="text-base font-semibold leading-7 tracking-tight text-gray-900 hover:underline">
                        {person.name}
                      </h3>
                    </Link>
                    <p className="text-sm font-semibold leading-6 text-indigo-600">
                      {person.role}
                    </p>
                  </div>
                </div>
              </li>
            </div>
          ))}
        </ul>
      </div>
    </div>
  );
}
