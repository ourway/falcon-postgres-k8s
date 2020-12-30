<script>
import { onMount, onDestroy } from "svelte";
let version;
let servertime;
let hitcount;
let server_interval;

async function get_server_time() {
  const res = await fetch("/api/v1/servertime");
  const data = await res.json();
  return data.response;
}

async function get_hit_count() {
  const res = await fetch("/api/v1/hitcount");
  const data = await res.json();
  return data.response;
}

onDestroy(() => clearInterval(server_interval));

onMount(async () => {
  const res1 = await fetch("/api/v1/ping");
  const data1 = await res1.json();
  version = data1.version;
  servertime = await get_server_time();
  hitcount = await get_hit_count();

  server_interval = setInterval(async () => {
    servertime = await get_server_time();
    hitcount = await get_hit_count();
  }, 1000);
});
</script>

<svelte:head>
  <title>FAL project</title>
</svelte:head>

<h1>Great version {version}!</h1>

<figure>
  <img height="300" width="100" alt="Success Kid" src="/strange.jpg" />
  <figcaption>server hitcount is {hitcount}</figcaption>
</figure>

<p><strong>ServerTime is: {servertime}</strong></p>

<style>
h1,
figure,
p {
  text-align: center;
  margin: 0 auto;
}

h1 {
  font-size: 2.8em;
  text-transform: uppercase;
  font-weight: 700;
  margin: 0 0 0.5em 0;
}

figure {
  margin: 0 0 1em 0;
}

img {
  width: 100%;
  max-width: 400px;
  margin: 0 0 1em 0;
}

p {
  margin: 1em auto;
}

@media (min-width: 480px) {
  h1 {
    font-size: 4em;
  }
}
</style>
