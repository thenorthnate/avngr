<template>
  <div>
    <table class="table is-fullwidth is-bordered is-scrollable is-hoverable">
      <thead>
        <tr>
          <th contenteditable>
            File
          </th>
          <th contenteditable>
            Size
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <button class="button is-small">
              <span>
                <font-awesome-icon icon="database" />
              </span>
              <span>File</span>
            </button>
          </td>
          <td contenteditable>
            TEST
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'shTable',
  data() {
    return {
      option: {},
    };
  },
};
</script>
