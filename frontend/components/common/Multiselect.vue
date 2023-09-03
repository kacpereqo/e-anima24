<template>
  <div class="autocomplete" ref="autocomplete">
    <div
      v-for="(selected, idx) in props.selecteds"
      :key="idx"
      class="selected"
      @click="selecteds.splice(idx, 1)"
    >
      {{ selected }}
    </div>
    <input
      class="form-control"
      type="store.series"
      v-model="text"
      @click.stop.prevent="show = true"
      @input="inputHandler"
      @keydown.backspace="backspaceHandler"
      @keydown.enter="enterHandler"
      @keydown.down="active++ && active >= matches.length && (active = 0)"
      @keydown.up="active-- && active < 0 && (active = matches.length - 1)"
    />
    <ul class="dropdown-menu" v-if="show" @click.stop>
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
const props = defineProps<{
  data: string[];
  addText?: {
    first: string;
    second: string;
  };
  selecteds: string[];
}>();

const emits = defineEmits<{
  (e: "update:props.selecteds", value: string[]): void;
}>();

const text = ref("");
const active = ref(-1);
const matches = ref([] as string[]);
const show = ref(false);
const autocomplete = ref<HTMLElement | null>(null);

onClickOutside(autocomplete, () => {
  show.value = false;
});

function enterHandler() {
  if (active.value >= 0 && matches.value[active.value]) {
    setMatch(matches.value[active.value]);
    active.value = -1;
  }
}

function backspaceHandler() {
  if (props.selecteds.length > 0 && text.value.length === 0) {
    props.selecteds.pop();
  }
}

function inputHandler() {
  if (text.value.length > 0) {
    matches.value = props.data.filter((item) => {
      return item.toLowerCase().indexOf(text.value.toLocaleLowerCase()) > -1;
    });
  } else {
    matches.value = [];
  }
}
function setMatch(value: string) {
  text.value = "";
  props.selecteds.push(value);
  emits("update:props.selecteds", props.selecteds);
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

.selected {
  background-color: var(--major-color);
  margin-right: 0.5rem;
  color: var(--font-color);
  font-size: 1.6rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  border-radius: 0.25rem;
  padding: 0.5rem;
  cursor: pointer;
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
  padding: 0.5rem;
  background-color: var(--major-color--light);
  position: relative;
  display: flex;
}

ul {
  position: absolute;
  top: 100%;
  left: 0;
  width: 100%;
  background-color: var(--major-color--light);
  border-radius: 0.25rem;
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
