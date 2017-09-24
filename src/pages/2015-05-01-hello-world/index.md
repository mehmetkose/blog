---
title: Hello World
date: "2015-05-01T22:12:03.284Z"
path: "/hello-world/"
---

This is my first post on my new fake blog! How exciting!

I'm sure I'll write a lot more interesting things in the future.

Oh, and here's a great quote from this Wikipedia on [salted duck eggs](http://en.wikipedia.org/wiki/Salted_duck_egg).

>A salted duck egg is a Chinese preserved food product made by soaking duck eggs in brine, or packing each egg in damp, salted charcoal. In Asian supermarkets, these eggs are sometimes sold covered in a thick layer of salted charcoal paste. The eggs may also be sold with the salted paste removed, wrapped in plastic, and vacuum packed. From the salt curing process, the salted duck eggs have a briny aroma, a gelatin-like egg white and a firm-textured, round yolk that is bright orange-red in color.


```js
  import React from 'react';
  import Websocket from 'react-websocket';

  class ProductDetail extends React.Component {

    constructor(props) {
      super(props);
      this.state = {
        count: 90
      };
    }

    handleData(data) {
      let result = JSON.parse(data);
      this.setState({count: this.state.count + result.movement});
    }

    render() {
      return (
        <div>
          Count: <strong>{this.state.count}</strong>

          <Websocket url='ws://localhost:8888/live/product/12345/'
              onMessage={this.handleData.bind(this)}/>
        </div>
      );
    }
  }

  export default ProductDetail;
```


![Chinese Salty Egg](./salty_egg.jpg)
