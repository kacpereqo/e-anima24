<template>
  <div
    class="autocomplete"
    ref="autocomplete"
    @click.stop.prevent="show = true"
  >
    <input
      class="form-control"
      type="store.series"
      v-model="store.series"
      @input="change"
      @keydown.enter="enterHandler"
      @keydown.down="active++ && active >= matches.length && (active = 0)"
      @keydown.up="active-- && active < 0 && (active = matches.length - 1)"
    />
    <ul
      class="dropdown-menu"
      v-if="store.series.length !== 0 && show"
      @click.stop
    >
      <li
        v-for="(suggestion, idx) in matches"
        @click="setMatch(suggestion)"
        :key="idx"
        :class="{ active: active === idx }"
      >
        {{ suggestion }}
      </li>
      <li class="add-series" v-if="matches.length < 5 && props.addText">
        <Icon name="material-symbols:add-box-outline-rounded" />
        <div>
          <span>{{ props.addText?.first }}</span>
          <span>{{ props.addText?.second }}</span>
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { useAddAnimeFormStore } from "@/stores/addAnimeStore";

const store = useAddAnimeFormStore();

const props = defineProps<{
  data: string[];
  addText?: {
    first: string;
    second: string;
  };
}>();

const data = ref([""]);
const active = ref(-1);
const matches = ref([] as string[]);
const show = ref(false);
const autocomplete = ref<HTMLElement | null>(null);

onClickOutside(autocomplete, () => {
  show.value = false;
});

function enterHandler() {
  if (active.value >= 0) {
    setMatch(matches.value[active.value]);
    active.value = -1;
  }
}

// watch for data changes

watch(
  () => props.data,
  () => {
    change();
  }
);
function change() {
  if (store.series.length > 0) {
    matches.value = props.data.filter((item: string) => {
      return item.toLowerCase().indexOf(store.series.toLowerCase()) > -1;
    });
  } else {
    matches.value = [];
  }
}
function setMatch(value: string) {
  store.series = value;
  show.value = false;
  matches.value = [];
}
</script>

<style scoped>
.active {
  background-color: var(--major-color);
}

input {
  width: 100%;
  padding: 0.5rem;
  border-radius: 0.25rem;
  font-size: 1rem;
  border: none;
  outline: transparent;
  background-color: var(--major-color--light);
  font-size: 1.6rem;
  color: var(--font-color);
}

.add-series {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: 500;
}

.add-series div {
  display: flex;
  flex-direction: column;
}
.add-series span:nth-child(1) {
  font-size: 1.2rem;
  font-weight: 700;
}
.autocomplete {
  position: relative;
  display: flex;
}

ul {
  position: absolute;
  top: calc(100% - 0.1rem);
  left: 0;
  width: 100%;
  background-color: var(--major-color--light);
  box-shadow: 1rem 1rem 1rem 0.2rem rgba(0, 0, 0, 0.3);
  border-radius: 0 0 0.25rem 0.25rem;
  padding: 0.5rem;
  list-style: none;
  z-index: 1000;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

li {
  padding: 1rem;
  border-radius: 0.25rem;
  cursor: pointer;
  transition: background-color 0.1s ease-in-out;
}

li:hover {
  background-color: var(--major-color);
}
</style>
