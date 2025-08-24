import React from "react";
import { FaGithub } from "react-icons/fa";

const Footer: React.FC = () => {
  return (
    <footer className="w-full bg-gray-900 text-gray-300 py-4 flex flex-col md:flex-row justify-between items-center px-6 md:px-12 border-t border-gray-700">
      <p className="text-sm md:text-base">Made by Aman</p>
      <a
        href="https://github.com/AmanTShekar"
        target="_blank"
        rel="noopener noreferrer"
        className="text-gray-300 hover:text-white transition text-2xl"
      >
        <FaGithub />
      </a>
    </footer>
  );
};

export default Footer;
