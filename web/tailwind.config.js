/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class",
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      width: {
        112: "28rem",
        128: "32rem",
        144: "36rem",
        160: "40rem",
        176: "44rem",
        192: "48rem",
      },
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "gradient-conic":
          "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
      },
      zIndex: {
        41: "41",
        42: "42",
        43: "43",
        44: "44",
        45: "45",
        46: "46",
        47: "47",
        48: "48",
        49: "49",
        50: "50",
      },
      colors: {
        gh: {
          gray: {
            0: "#f6f8fa",
            1: "#eaeef2",
            2: "#d0d7de",
            3: "#afb8c1",
            4: "#8c959f",
            5: "#6e7781",
            6: "#57606a",
            7: "#424a53",
            8: "#32383f",
            9: "#24292f",
          },
          blue: {
            0: "#ddf4ff",
            1: "#b6e3ff",
            2: "#80ccff",
            3: "#54aeff",
            4: "#218bff",
            5: "#0969da",
            6: "#0550ae",
            7: "#033d8b",
            8: "#0a3069",
            9: "#002155",
          },
          green: {
            0: "#dafbe1",
            1: "#aceebb",
            2: "#6fdd8b",
            3: "#4ac26b",
            4: "#2da44e",
            5: "#1a7f37",
            6: "#116329",
            7: "#044f1e",
            8: "#003d16",
            9: "#002d11",
          },
          yellow: {
            0: "#fff8c5",
            1: "#fae17d",
            2: "#eac54f",
            3: "#d4a72c",
            4: "#bf8700",
            5: "#9a6700",
            6: "#7d4e00",
            7: "#633c01",
            8: "#4d2d00",
            9: "#3b2300",
          },
          orange: {
            0: "#fff1e5",
            1: "#ffd8b5",
            2: "#ffb77c",
            3: "#fb8f44",
            4: "#e16f24",
            5: "#bc4c00",
            6: "#953800",
            7: "#762c00",
            8: "#5c2200",
            9: "#471700",
          },
          red: {
            0: "#ffebe9",
            1: "#ffcecb",
            2: "#ffaba8",
            3: "#ff8182",
            4: "#fa4549",
            5: "#cf222e",
            6: "#a40e26",
            7: "#82071e",
            8: "#660018",
            9: "#4c0014",
          },
          purple: {
            0: "#fbefff",
            1: "#ecd8ff",
            2: "#d8b9ff",
            3: "#c297ff",
            4: "#a475f9",
            5: "#8250df",
            6: "#6639ba",
            7: "#512a97",
            8: "#3e1f79",
            9: "#2e1461",
          },
          pink: {
            0: "#ffeff7",
            1: "#ffd3eb",
            2: "#ffadda",
            3: "#ff80c8",
            4: "#e85aad",
            5: "#bf3989",
            6: "#99286e",
            7: "#772057",
            8: "#611347",
            9: "#4d0336",
          },
          coral: {
            0: "#fff0eb",
            1: "#ffd6cc",
            2: "#ffb4a1",
            3: "#fd8c73",
            4: "#ec6547",
            5: "#c4432b",
            6: "#9e2f1c",
            7: "#801f0f",
            8: "#691105",
            9: "#510901",
          },
          border: "#d0d7de", //same as gray-2
          bg: "#f6f8fa", //same as gray-0
          darkbg: "#24292f", //same as gray-9
          subtledarkbg: "#32383f", //same as gray-8
          darkborder: "#424a53", //same as gray-7
          text: {
            primary: "#24292f", //same as gray-9
            secondary: "#57606a", //same as gray-6
            tertiary: "#6e7781", //same as gray-5
          },
          dark: {
            border: "#424a53", //same as gray-7
            bg: "#24292f", //same as gray-9
            text: {
              primary: "#f6f8fa", //same as gray-0
              secondary: "#afb8c1", //same as gray-3
              tertiary: "#8c959f", //same as gray-4
            },
          },
        },
      },
    },
  },
};
