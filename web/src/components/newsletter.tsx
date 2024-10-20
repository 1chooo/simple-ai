import React from "react";
import { MailIcon } from "@primer/octicons-react";

export default function Newsletter() {
  return (
    <div className="mb-10 bg-gh-bg bg-gradient-to-br from-gh-blue-1/80 to-gh-purple-1/60 p-8 sm:p-16 mx-auto sm:rounded-[48px] grid grid-cols-12 relative border-0 sm:border border-gh-border">
      <div className="col-span-1 hidden lg:block">
        <div className="w-12 h-12 flex items-center justify-center -left-2 top-2 transform translate-x-px relative border-2 rounded-full bg-gh-bg border-gh-border z-20">
          <MailIcon className={"text-gh-gray-4 w-5 h-5"} />
        </div>
      </div>
      <div className="mt-1 col-span-12 lg:col-span-10 lg:col-start-2 mb-8">
        <h2 className="text-3xl font-bold tracking-tight text-gh-text-primary sm:text-5xl">
          Newsletter
        </h2>

        <h3 className={"mt-2 text-gh-text-secondary text-lg"}>
          Subscribe to our newsletter.
        </h3>
      </div>
      <div className="col-span-1 col-start-1 hidden lg:block">
        <div className="border-l-2 border-gh-gray-0/80 h-full absolute left-20 top-0 z-10"></div>
      </div>
      <div className="col-span-12 lg:col-span-10 lg:col-start-2 mt-3 lg:w-[990px]">
        <form
          action="https://postal.hackclub.com/subscribe"
          method="POST"
          acceptCharset="utf-8"
          className="w-full"
        >
          <div className="mb-4">
            <label htmlFor="name" className="mb-1 block text-gh-text-primary">
              Name
            </label>
            <input
              type="text"
              name="name"
              id="name"
              className="w-full rounded-md border border-gh-border px-3 py-2 bg-gh-bg outline-none focus:outline-none focus:border-gh-purple-7/30 focus:bg-gh-white transition-all text-gh-text-primary"
              required={true}
            />
          </div>
          <div className="mb-4">
            <label htmlFor="email" className="mb-1 block text-gh-text-primary">
              Email
            </label>
            <input
              type="email"
              name="email"
              id="email"
              className="w-full rounded-md border border-gh-border px-3 py-2 bg-gh-bg outline-none focus:outline-none focus:border-gh-purple-7/30 focus:bg-gh-white transition-all text-gh-text-primary"
              required={true}
            />
          </div>
          <div className="hidden">
            <label htmlFor="hp" className="mb-1 block">
              HP
            </label>
            <input
              type="text"
              name="hp"
              id="hp"
              className="w-full rounded-md border border-gray-300 px-3 py-2 bg-gh-bg"
            />
          </div>
          <input type="hidden" name="list" value="1AaBEdR4lS7PwHFOfEzGtQ" />
          <input type="hidden" name="subform" value="yes" />

          <input
            type="submit"
            name="submit"
            id="submit"
            className="cursor-pointer mt-4 rounded-lg border border-gh-border bg-gh-blue-3 px-4 py-2 font-semibold text-gh-dark-text-primary hover:bg-gh-purple-5 hover:bordr-gh-purple-2/20 transition-all"
            value="Subscribe"
          />
          <p className={"text-gh-text-secondary text-xs mt-3 w-full"}>
            We’ll send you an email no more than once a month, when we work on
            something cool for you. You can unsubscribe at any time.
          </p>
        </form>
      </div>
    </div>
  );
}
