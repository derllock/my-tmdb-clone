<template>
  <div class="min-h-screen bg-slate-900 text-white">
    <!-- TOP NAV (fixed) -->
    <header
      class="fixed inset-x-0 top-0 z-30 bg-slate-900/90 backdrop-blur-sm border-b border-slate-800"
    >
      <div
        class="max-w-6xl mx-auto px-4 md:px-6 h-16 flex items-center justify-between"
      >
        <!-- Left: hamburger (mobile) / brand -->
        <div class="flex items-center gap-4">
          <button
            class="md:hidden p-2 rounded hover:bg-slate-800"
            aria-label="Open menu"
            @click="sidebarOpen = true"
          >
            <!-- hamburger -->
            <div class="w-5 h-0.5 bg-white mb-1"></div>
            <div class="w-5 h-0.5 bg-white mb-1"></div>
            <div class="w-5 h-0.5 bg-white"></div>
          </button>

          <div class="flex items-center gap-2">
            <div class="font-extrabold text-xl tracking-wide text-emerald-300">
              TMDB
            </div>
            <div class="hidden md:block text-slate-400 text-sm">
              The Movie Database
            </div>
          </div>
        </div>

        <!-- Center nav (desktop) -->
        <nav class="hidden md:flex items-center gap-6 text-sm text-slate-200">
          <a class="hover:underline" href="#">Movies</a>
          <a class="hover:underline" href="#">TV Shows</a>
          <a class="hover:underline" href="#">People</a>
          <a class="hover:underline" href="#">More</a>
        </nav>

        <!-- Right: login/join/search -->
        <div class="flex items-center gap-4">
          <div class="hidden md:flex items-center gap-3">
            <button class="px-3 py-1 rounded text-sm border border-slate-700">
              + Add
            </button>
            <button class="px-3 py-1 rounded text-sm">EN</button>
            <button class="px-3 py-1 rounded text-sm">Login</button>
            <button
              class="px-3 py-1 rounded bg-emerald-500 text-slate-900 font-semibold"
            >
              Join TMDB
            </button>
          </div>

          <!-- search icon placeholder -->
          <button class="p-2 rounded hover:bg-slate-800 text-sm">Search</button>
        </div>
      </div>
    </header>

    <!-- Mobile Sidebar -->
    <transition name="slide">
      <div
        v-if="sidebarOpen"
        class="fixed inset-0 z-40 flex"
        aria-hidden="false"
      >
        <div
          class="fixed inset-0 bg-black/50"
          @click="sidebarOpen = false"
        ></div>

        <aside
          class="relative w-72 max-w-full bg-slate-900 border-r border-slate-800 p-4"
        >
          <button
            class="mb-4 p-2 rounded hover:bg-slate-800"
            @click="sidebarOpen = false"
          >
            Close
          </button>
          <nav class="flex flex-col gap-3">
            <a href="#" class="py-2 px-2 rounded hover:bg-slate-800">Movies</a>
            <a href="#" class="py-2 px-2 rounded hover:bg-slate-800"
              >TV Shows</a
            >
            <a href="#" class="py-2 px-2 rounded hover:bg-slate-800">People</a>
            <a href="#" class="py-2 px-2 rounded hover:bg-slate-800">More</a>
            <div class="border-t border-slate-800 mt-3 pt-3">
              <a href="#" class="block py-2 px-2 rounded hover:bg-slate-800"
                >Login</a
              >
              <a
                href="#"
                class="block py-2 px-2 rounded bg-emerald-600 text-slate-900 mt-2"
                >Join TMDB</a
              >
            </div>
          </nav>
        </aside>
      </div>
    </transition>

    <!-- PAGE CONTENT -->
    <main class="pt-20">
      <!-- Hero (uses poster as background with overlay) -->
      <section class="relative" :style="heroStyle">
        <div
          class="absolute inset-0 bg-gradient-to-b from-slate-900/80 via-slate-900/60 to-slate-900/90"
        ></div>

        <div class="max-w-6xl mx-auto px-4 md:px-6 py-8">
          <div class="flex flex-col md:flex-row md:items-start gap-6">
            <!-- Poster column -->
            <div class="flex-shrink-0">
              <img
                v-if="movie.Poster && movie.Poster !== 'N/A'"
                :src="movie.Poster"
                :alt="movie.Title"
                class="w-48 md:w-64 rounded-lg shadow-2xl border border-slate-800"
              />
              <!-- small streaming tile under poster (like screenshot) -->
              <div
                class="mt-4 bg-slate-800 p-3 rounded text-sm hidden md:block"
              >
                <div class="font-semibold">Now Streaming</div>
                <div class="text-slate-300">Watch Now</div>
              </div>
            </div>

            <!-- Info column -->
            <div class="flex-1 text-white">
              <!-- Title -->
              <h1 class="text-2xl md:text-4xl font-bold leading-tight">
                {{ movie.Title }}
                <span class="text-lg font-normal text-slate-300"
                  >({{ movie.Year }})</span
                >
              </h1>

              <!-- Subline: released / runtime / genre -->
              <div
                class="mt-3 text-slate-300 flex flex-wrap items-center gap-3"
              >
                <span
                  class="px-2 py-1 border rounded border-slate-700 text-sm"
                  >{{ movie.Rated }}</span
                >
                <span class="text-sm">{{ movie.Released }}</span>
                <span class="hidden md:inline">•</span>
                <span class="text-sm">{{ movie.Runtime }}</span>
                <span class="hidden md:inline">•</span>
                <span class="text-sm">{{ movie.Genre }}</span>
              </div>

              <!-- Ratings row -->
              <div class="mt-6 flex flex-wrap items-center gap-4">
                <!-- IMDb circle -->
                <div v-if="imdbRating" class="flex items-center gap-3">
                  <div
                    class="w-14 h-14 rounded-full flex items-center justify-center"
                    :style="imdbCircleStyle"
                  >
                    <span class="font-bold text-sm">{{ imdbRating }}</span>
                  </div>
                  <div class="text-sm text-slate-300">User Score</div>
                </div>

                <!-- Other badges -->
                <div class="flex items-center gap-2">
                  <span
                    v-for="r in extraRatings"
                    :key="r.Source"
                    :class="
                      badgeColor(r.Source) +
                      ' px-2 py-1 rounded text-sm font-medium'
                    "
                  >
                    {{ r.Source }}: {{ r.Value }}
                  </span>
                </div>

                <!-- simple actions -->
                <div class="flex gap-4">
                  <button class="px-4 py-2 bg-blue-600 text-white rounded">
                    👍 Like
                  </button>
                  <button class="px-4 py-2 bg-gray-700 text-white rounded">
                    🔖 Bookmark
                  </button>
                  <button class="px-4 py-2 bg-green-600 text-white rounded">
                    ➕ Add to List
                  </button>
                </div>
                <!-- BottomBar.vue -->
                <div
                  class="fixed bottom-0 left-0 w-full flex justify-around bg-gray-900 text-white py-3 md:hidden"
                >
                  <button>👍</button>
                  <button>🔖</button>
                  <button>➕</button>
                </div>
              </div>

              <!-- Overview -->
              <div class="mt-8">
                <h2 class="mt-2 text-xl md:text-2xl font-semibold">Overview</h2>
                <p class="mt-3 text-slate-200 max-w-3xl">
                  {{ movie.Plot }}
                </p>
              </div>

              <!-- Credits block simplified -->
              <div
                class="mt-8 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 text-sm"
              >
                <div>
                  <div class="font-semibold">Director</div>
                  <div class="text-slate-300">{{ movie.Director }}</div>
                </div>
                <div>
                  <div class="font-semibold">Writers</div>
                  <div class="text-slate-300">{{ movie.Writer }}</div>
                </div>
                <div>
                  <div class="font-semibold">Stars</div>
                  <div class="text-slate-300">{{ movie.Actors }}</div>
                </div>
              </div>
            </div>
            <!-- end info col -->
          </div>
          <!-- end flex row -->
        </div>
        <!-- end container -->
      </section>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";

const movie = ref({});
const sidebarOpen = ref(false);

onMounted(async () => {
  // use HTTPS to avoid mixed-content issues
  const res = await fetch(
    "https://www.omdbapi.com/?i=tt3896198&apikey=d2132124"
  );
  movie.value = await res.json();
});

// computed helpers
const imdbRating = computed(() => {
  return movie.value.imdbRating ? movie.value.imdbRating : "";
});

// compute color-coded extra ratings (Rotten, Metacritic)
const extraRatings = computed(() => {
  if (!movie.value.Ratings) return [];
  return movie.value.Ratings.filter((r) =>
    ["Rotten Tomatoes", "Metacritic"].includes(r.Source)
  );
});

const badgeColor = (source) => {
  switch (source) {
    case "Rotten Tomatoes":
      return "bg-red-600";
    case "Metacritic":
      return "bg-yellow-400 text-black";
    default:
      return "bg-slate-700";
  }
};

// hero style uses poster as background (subtle, darkened via overlay)
const heroStyle = computed(() => {
  if (movie.value.Poster && movie.value.Poster !== "N/A") {
    return {
      backgroundImage: `linear-gradient(rgba(2,6,23,0.6), rgba(2,6,23,0.6)), url(${movie.value.Poster})`,
      backgroundSize: "cover",
      backgroundPosition: "center",
    };
  }
  return { backgroundColor: "#0f1724" };
});

// compute simple circle style for imdb (green with inner ring)
// If you want an actual percentage ring, replace with svg or conic-gradient
const imdbCircleStyle = computed(() => {
  const val = parseFloat(movie.value.imdbRating || 0);
  // green shade darkens a bit when rating low
  const bg = val >= 7.5 ? "#16a34a" : val >= 6 ? "#22c55e" : "#94a3b8";
  return {
    background: bg,
    color: "white",
    border: "4px solid rgba(0,0,0,0.25)",
  };
});
</script>

<style>
/* small slide animation for sidebar */
.slide-enter-from {
  transform: translateX(-100%);
}
.slide-enter-active {
  transition: transform 0.18s ease-out;
}
.slide-leave-to {
  transform: translateX(-100%);
}
.slide-leave-active {
  transition: transform 0.18s ease-in;
}
</style>
