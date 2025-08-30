<template>
  <nav class="bg-black text-white px-6 py-3">
    <ul class="flex gap-6 justify-center">
      <!-- Overview Dropdown -->
      <li class="relative group">
        <button class="hover:text-blue-400">Overview ▾</button>
        <ul
          class="absolute left-0 mt-px hidden group-hover:block bg-gray-800 rounded shadow-lg w-48 z-40 transition-opacity duration-200 opacity-0 group-hover:opacity-100"
        >
          <li class="px-4 py-2 hover:bg-gray-700 cursor-pointer">Main</li>
          <li class="px-4 py-2 hover:bg-gray-700 cursor-pointer">
            Cast & Crews
          </li>
          <li class="px-4 py-2 hover:bg-gray-700 cursor-pointer">
            Release Date
          </li>
        </ul>
      </li>

      <!-- Media Dropdown -->
      <li class="relative group">
        <button class="hover:text-blue-400">Media ▾</button>
        <ul
          class="absolute left-0 mt-px hidden group-hover:block bg-gray-800 rounded shadow-lg w-48 z-40 transition-opacity duration-200 opacity-0 group-hover:opacity-100"
        >
          <li class="px-4 py-2 hover:bg-gray-700 cursor-pointer">Backdrops</li>
          <li class="px-4 py-2 hover:bg-gray-700 cursor-pointer">Logos</li>
          <li class="px-4 py-2 hover:bg-gray-700 cursor-pointer">Posters</li>
        </ul>
      </li>

      <!-- Fandom Dropdown -->
      <li class="relative group">
        <button class="hover:text-blue-400">Fandom ▾</button>
        <ul
          class="absolute left-0 mt-px hidden group-hover:block bg-gray-800 rounded shadow-lg w-48 z-40 transition-opacity duration-200 opacity-0 group-hover:opacity-100"
        >
          <li class="px-4 py-2 hover:bg-gray-700 cursor-pointer">Discussion</li>
          <li class="px-4 py-2 hover:bg-gray-700 cursor-pointer">Reviews</li>
        </ul>
      </li>

      <!-- Share Dropdown -->
      <li class="relative group">
        <button class="hover:text-blue-400">Share ▾</button>
        <ul
          class="absolute left-0 mt-px hidden group-hover:block bg-gray-800 rounded shadow-lg w-48 z-40 transition-opacity duration-200 opacity-0 group-hover:opacity-100"
        >
          <li class="px-4 py-2 hover:bg-gray-700 cursor-pointer">Share Link</li>
          <li class="px-4 py-2 hover:bg-gray-700 cursor-pointer">Facebook</li>
          <li class="px-4 py-2 hover:bg-gray-700 cursor-pointer">Tweet</li>
        </ul>
      </li>
    </ul>
  </nav>
</template>
