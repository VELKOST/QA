import http from 'k6/http';
import { check } from 'k6';

export const options = {
  // значения по умолчанию; будем переопределять из CLI
};

const TARGET = __ENV.TARGET || 'https://example.com'; // укажите свой URL

export default function () {
  const res = http.get(TARGET, { tags: { name: 'GET_' + TARGET } });
  check(res, {
    'status is 200': (r) => r.status === 200,
  });
}
