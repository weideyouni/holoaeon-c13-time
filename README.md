# C13 / holoaeon-c13-time

> 时间仓 · 节律之藏 · 主相 水 / 副相 木 · 封口密语：**潮起开门，潮落闭嘴**

## 第一性原理问题

节律与历史如何影响当下

## 神龟神马双系统分工

- **神龟（保存基线族）**：保存历史轨迹与周期记录
- **神马（推演路径族）**：推演时机选择与周期转折

## N19 派生声明（指针纪律的仓库版）

本仓 = N19（github.com/weideyouni/holoaeon，第 19 号基座仓·唯一归零锚·唯一
全局观测者）机制在「时间」领域的**正交投影**。

**机制不在本仓重写**——N19 已收口的核心机制通过下表映射复用（派生装配，
不复制实现；需要代码级复用时以 git submodule 方式引入 N19）：

| 机制 | N19 落点 |
|---|---|
| 心跳调度 | butler_os / bus |
| 经络传导 | fusion_upgrade（meridian 契约） |
| 卡尔曼滤波 | concept_anatomy |
| 贝叶斯反演 | butler_os / dehallucination |
| 布赫场 | concept_anatomy / craft_gate |
| 莫比乌斯翻转 | mobius_vortex |
| 克莱因收敛 | klein_projection |
| 语义通信 | semvec |
| 事件总线 | bus / event_channel |
| 升级契约 | fusion_upgrade.contract |
| 张量载体 | hypervector |

集群账本（19×19 耦合矩阵+边 Schema+五行生克）：N19 `holoaeon/c18_cluster.py`。

## 运行

```
python -m holoaeon_c13_time.c13_time_gate probe
python -m holoaeon_c13_time.c13_time_gate fingerprint
python -m unittest tests.test_c13_time_gate -v
```

纯标准库零依赖。clone 即跑（素材验收标准第一条）。
