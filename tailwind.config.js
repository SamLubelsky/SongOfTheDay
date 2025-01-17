/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js"
  ],
  theme: {
    spacing:{
      '1':'4px',
      '2':'8px',
      '3':'12px',
      '4':'16px',
      '5':'24px',
      '6':'32px',
      '7':'48px',
      '8':'64px',
      '9':'96px',
      '10':'128px',
      '11':'192px',
      '12':'256px',
      '13':'384px',
      '14':'512px',
      '15':'640px',
      '16':'768px',
    },
    fontSize: {
      '1':'12px',
      '2':'14px',
      '3':'16px',
      '4':'18px',
      '5':'20px',
      '6':'24px',
      '7':'30px',
      '8':'36px',
      '9':'48px',
      '10':'60px',
      '11':'72px',
    },
    extend: {},
  },
  plugins: [],
}

