export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  if (!weakMap.has(endpoint)) {
    weakMap.set(endpoint, 0);
  }

  const count = weakMap.get(endpoint);
  weakMap.set(endpoint, count + 1);

  if (weakMap.get(endpoint) >= 5) {
    throw new Error('Endpoint load is high');
  }
}
