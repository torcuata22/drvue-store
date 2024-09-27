<template>
    <div class="page-cart">
        <div class="columns is-multiline">
            <div class="title">Cart</div>
        </div>
        <div class="column is-12 box">
            <table class="table is-fullwidth" v-if="cart.totalLength">
                <thead>
                    <tr>
                        <th>Product</th>
                        <th>Quantity</th>
                        <th>Price</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    <CartItem
                        v-for="item in cart.items"
                        v-bind:key="item.product.id"
                        v-bind:initialItem="item"
                        />
                </tbody>
            </table>
            <p v-else>Your cart is empty</p>
        </div>
    </div>

</template>

<script>

export default {
    name: 'Cart'
}
</script>