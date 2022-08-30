<template>
  <div id="loading">
    <img
      class="img"
      src="../assets/Spinner-0.9s-250px.gif"
      alt="loading..."
      width="200"
    />
    <div class="loading-text">
        <p id="loading-text">...در حال بارگذاری اخبار، لطفا شکیبا باشید</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Loading"
};
</script>

<style>
#loading {
    position: fixed;
    margin-left: auto;
    margin-right: auto;
    display: block;
    z-index: 100;
    width: 100%;
    height: 100%;
    background-color:rgba(153, 153, 153, 0.5);
}
.img {
    margin-top: 14%;
}

.loading-text {
    background-color: rgba(255, 255, 255, 0.7);
    width: 35%;
    margin: auto;

    border: 2px solid #00d1b2;
    padding: 10px;
    border-radius: 25px;
}

#loading-text{  
    color: black;
    font-size: large;
    text-shadow: 3px 3px 10px white;
}
</style>