---
tags:
  - Vue
  - 前端
---
Vue Router 是 Vue.js 官方的路由管理器，用于构建单页面应用（SPA）。本文介绍 Vue Router 4.x 版本在 Vue3 中的使用方法。

## 目录

- [安装与配置](#安装与配置)
- [基本使用](#基本使用)
- [router-link 组件](#router-link-组件)
- [router-view 组件](#router-view-组件)
- [编程式导航](#编程式导航)
- [动态路由](#动态路由)
- [嵌套路由](#嵌套路由)
- [路由守卫](#路由守卫)

## 安装与配置

### 安装依赖

```bash
npm install vue-router
```

### 创建路由配置

在 `router/index.js` 中创建路由实例：

```javascript
import { createRouter, createWebHistory } from "vue-router";

// 定义路由配置
const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("../views/Home.vue"),
  },
  {
    path: "/about",
    name: "About",
    component: () => import("../views/About.vue"),
  },
];

// 创建路由实例
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
```

### 注册路由

在 `main.js` 中注册路由：

```javascript
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

const app = createApp(App);
app.use(router);
app.mount('#app');
```

## 基本使用

### 创建页面组件

**views/Home.vue**

```vue
<script setup>
</script>

<template>
  <div class="page">
    <h2>Home Page</h2>
    <router-link to="/about">Go to About</router-link>
  </div>
</template>

<style scoped>
.page {
  padding: 20px;
}
</style>
```

**views/About.vue**

```vue
<script setup>
</script>

<template>
  <div class="page">
    <h2>About Page</h2>
    <router-link to="/">Go to Home</router-link>
  </div>
</template>

<style scoped>
.page {
  padding: 20px;
}
</style>
```

### App.vue 配置

```vue
<script setup>
</script>

<template>
  <router-view v-slot="{ Component }">
    <transition name="fade" mode="out-in">
      <component :is="Component" />
    </transition>
  </router-view>
</template>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
```

## router-link 组件

`<router-link>` 用于声明式导航，默认渲染为 `<a>` 标签。

### 基本属性

| 属性 | 说明 |
|------|------|
| `to` | 目标路由地址 |
| `replace` | 替换历史记录，不留下新记录 |
| `active-class` | 激活时应用的 CSS 类名 |
| `exact-active-class` | 精确匹配时应用的 CSS 类名 |
| `custom` | 自定义渲染，需配合 v-slot |

### to 属性用法

**字符串形式**

```vue
<router-link to="/about">About</router-link>
```

**对象形式**

```vue
<!-- 路径跳转 -->
<router-link :to="{ path: '/about' }">About</router-link>

<!-- 命名路由 -->
<router-link :to="{ name: 'About' }">About</router-link>

<!-- 带查询参数 -->
<router-link :to="{ path: '/user', query: { id: 123 } }">User</router-link>
```

### replace 属性

```vue
<router-link to="/about" replace>About</router-link>
```

### 激活状态样式

```vue
<router-link
  to="/about"
  active-class="active"
  exact-active-class="exact-active"
>
  About
</router-link>
```

### 自定义渲染（Vue Router 4）

```vue
<router-link to="/about" custom v-slot="{ navigate, isActive }">
  <button @click="navigate" :class="{ active: isActive }">
    About
  </button>
</router-link>
```

## router-view 组件

`<router-view>` 用于渲染匹配的路由组件。

### 基本用法

```vue
<router-view />
```

### 配合过渡效果

```vue
<router-view v-slot="{ Component }">
  <transition name="fade" mode="out-in">
    <component :is="Component" />
  </transition>
</router-view>
```

### 命名视图

用于同时渲染多个视图：

```javascript
const routes = [
  {
    path: '/layout',
    components: {
      default: Home,
      header: Header,
      footer: Footer,
    },
  },
];
```

```vue
<router-view />
<router-view name="header" />
<router-view name="footer" />
```

## 编程式导航

在组件中使用 `useRouter` 进行编程式导航：

```vue
<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

const goToAbout = () => {
  router.push('/about');
};
</script>
```

### 导航方法

| 方法 | 说明 |
|------|------|
| `router.push()` | 跳转并保留历史记录 |
| `router.replace()` | 跳转并替换历史记录 |
| `router.go(n)` | 前进/后退 n 步 |
| `router.back()` | 后退一步 |
| `router.forward()` | 前进一步 |

### 使用示例

```javascript
import { useRouter } from 'vue-router';

const router = useRouter();

// push 用法
router.push('/about');
router.push({ path: '/about' });
router.push({ name: 'About' });
router.push({ path: '/user', query: { id: 123 } });

// replace 用法
router.replace('/about');

// 历史导航
router.go(-1);    // 后退一步
router.back();    // 后退一步
router.forward(); // 前进一步
```

## 动态路由

### 路由参数

```javascript
const routes = [
  {
    path: '/user/:id',
    name: 'User',
    component: () => import('../views/User.vue'),
  },
];
```

### 获取路由参数

```vue
<script setup>
import { useRoute } from 'vue-router';

const route = useRoute();
const userId = route.params.id;
</script>

<template>
  <div>User ID: {{ userId }}</div>
</template>
```

### 监听路由变化

```vue
<script setup>
import { watch } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();

watch(
  () => route.params.id,
  (newId) => {
    console.log('User ID changed:', newId);
  }
);
</script>
```

## 嵌套路由

### 路由配置

```javascript
const routes = [
  {
    path: '/user',
    component: () => import('../views/User.vue'),
    children: [
      {
        path: '',           // 默认子路由
        name: 'UserHome',
        component: () => import('../views/UserHome.vue'),
      },
      {
        path: 'profile',    // /user/profile
        name: 'UserProfile',
        component: () => import('../views/UserProfile.vue'),
      },
      {
        path: 'settings',   // /user/settings
        name: 'UserSettings',
        component: () => import('../views/UserSettings.vue'),
      },
    ],
  },
];
```

### 父组件中使用 router-view

```vue
<!-- User.vue -->
<template>
  <div>
    <h2>User Page</h2>
    <nav>
      <router-link to="/user">Home</router-link>
      <router-link to="/user/profile">Profile</router-link>
      <router-link to="/user/settings">Settings</router-link>
    </nav>
    <router-view />
  </div>
</template>
```

## 路由守卫

### 全局前置守卫

```javascript
// router/index.js
router.beforeEach((to, from, next) => {
  const isAuthenticated = checkAuth();

  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/login');
  } else {
    next();
  }
});
```

### 路由元信息

```javascript
const routes = [
  {
    path: '/admin',
    name: 'Admin',
    component: Admin,
    meta: { requiresAuth: true },
  },
];
```

### 组件内守卫

```vue
<script setup>
import { onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router';

// 离开前确认
onBeforeRouteLeave((to, from, next) => {
  if (confirm('确定要离开吗？')) {
    next();
  } else {
    next(false);
  }
});

// 路由更新时
onBeforeRouteUpdate((to, from, next) => {
  console.log('Route updated');
  next();
});
</script>
```

## History 模式

### HTML5 History 模式

```javascript
import { createRouter, createWebHistory } from 'vue-router';

const router = createRouter({
  history: createWebHistory(),
  routes,
});
```

### Hash 模式

```javascript
import { createRouter, createWebHashHistory } from 'vue-router';

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});
```

### Memory 模式（适用于非浏览器环境）

```javascript
import { createRouter, createMemoryHistory } from 'vue-router';

const router = createRouter({
  history: createMemoryHistory(),
  routes,
});
```

## 常见问题

### 404 页面处理

```javascript
const routes = [
  // ...其他路由
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('../views/NotFound.vue'),
  },
];
```

### 路由懒加载

```javascript
// 推荐：使用动态导入
component: () => import('../views/About.vue');

// 分组打包
component: () => import(/* webpackChunkName: "about" */ '../views/About.vue');
```

### 滚动行为

```javascript
const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    } else if (to.hash) {
      return { el: to.hash };
    } else {
      return { top: 0 };
    }
  },
});
```
