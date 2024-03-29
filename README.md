# XianQi_BackEnd

掀棋是一种局势非常动态，对抗性很强的牌类游戏（尽管它通常使用象棋子进行游戏，但很明显也可以用合适的扑克牌来替代）。游戏进行的单位为局，每局结束后进行筹码结算，每个玩家的目标是赢得尽可能多的筹码。

## 掀棋规则：

### 使用道具
游戏使用中国象棋棋子进行，开始时去除双方的帅/将，一个炮，两个兵/卒，还剩下24张棋子，分别是红黑士，红黑相/象（以下均称为相），红黑马，红黑车，红黑炮各一（掀棋中称为狗），红黑兵卒各三（掀棋中称为牛）。

此外，还需要若干计分用的筹码。开始时没人同等分配同样多的筹码（建议至少10个）。

### 棋子大小
一张棋：士>相>马>车=同色的狗>牛，红>黑
两张棋：狗脚对=红士对>黑士对（剩余同一张棋的大小序列）
三张棋：三红牛>三黑牛

### 游戏流程
1. 用骰子或者接棋的方式来确定先揭棋/先出棋的玩家。所有棋子洗匀后三个玩家轮流（本游戏中所有的顺序都是逆时针顺序）接棋。
2. 首位接棋的玩家决定是否要继续进行这局游戏。通常来讲，如果ta判断赢面较大，ta会愿意进行这局游戏，否则的话ta可以选择**扣棋**。
3. 如果选择出棋的话，玩家可以出一个棋，完全相同的两个棋（或两个不同色的狗，此事被称为**狗脚对**），完全相同的三个棋（只有牛才可能）。
4. 后续玩家如果有完全可以大过前面玩家本轮所出的最大棋子组合的棋子组合（注意，相同大小无法大过对方，例如前一名玩家如果出了红士，后面玩家即使拥有红士，也无法大过对方），就*必须*将该棋子组合打出，否则的话就需要选择相同张数的低价值棋子进行**垫棋**，垫棋棋子朝下防止，其余玩家不得翻看。一轮结束后，所有玩家手中剩余的棋子数应当相同。本轮所有棋子归打出的棋子组合最大的玩家所有。打出的棋子每三张称之为一**柱**棋。拥有的棋子柱数会用于结算游戏筹码。
5. 一轮游戏结束后，由棋子组合最大的玩家开始决定是否出棋/扣棋。出棋情况如前所述。如果扣棋的话，剩余玩家需要决定是否**掀棋**。决定掀棋的顺序为，如果本局中之前有玩家掀过，那么就由最后一个掀过棋的玩家决定是否掀棋。否则就逆时针决定。扣棋玩家之外如果没有玩家愿意“掀棋”，则游戏结束，进入结算。否则的话，掀棋玩家将对扣棋玩家形成**一掀**，这种关系将用于结算筹码。
6. 如果某位玩家在开局时不拥有任何的士/相，则称为**黑**了，本局游戏直接结束。

### 结算筹码
1. 如果一名玩家拥有大于等于3柱棋少于6柱棋，则称为ta**够**了。如果一名玩家拥有大于等于6柱棋，则称为ta**瓷**了。
2. 如果一名玩家在没有够棋的时候进行了掀棋，游戏结束时，如果ta没有够棋，ta要为每次掀棋向扣棋方付出1枚筹码。
3. 每一名没有够棋的玩家要向每一名够棋玩家付出1枚筹码，向每一名瓷棋玩家付出3枚筹码。
5. 如果一名玩家在已经够棋的情况下进行了掀棋，游戏结束时，如果ta没有瓷棋，没有够棋的玩家将不用向ta支付够棋筹码（扣棋筹码依然需要结算）。

### 额外规则
以下的额外规则可以在游戏开始时选择启用或不启用。
1. 掀瓷包瓷：如果玩家A在玩家B选择掀棋之后的一轮瓷了，玩家B就需要向玩家A支付全部瓷棋筹码，玩家C不再需要支付瓷棋筹码。注意掀棋筹码需要额外计算。
2. 第一盘没瓷没扣：第一局游戏中，所有玩家在没有够棋的情况下都不允许扣棋。同时，瓷棋的筹码结算同够棋相同。
3. 抱头：如果有一名额外的玩家，每局游戏将随机（用骰子或揭棋）选出一名玩家进行抱头。抱头玩家的输赢将与ta右手的玩家相同。例如，如果只有ta右手边的玩家赢了，剩余两名玩家在一人给ta右手边的玩家一枚筹码的时候，还需要再给ta一枚筹码。此外，瓷棋的结算单位将变为4枚——没有抱头人的玩家将赢得12枚筹码（每人4枚），有抱头人的玩家和抱ta头的玩家将赢得8枚筹码（剩余两名玩家各出8枚）。
4. 接棋决定先出棋的一方：3人游戏时上一局的唯一输家/唯一赢家/无人够棋时的最后一个扣棋方/黑棋方随机抽选一张棋子，决定ta的出棋顺序：马和车先出，相和牛第二个出，士和炮第三个出。4人游戏时上一局未参与游戏的抱头人随机抽选，车先出，马第二个出，相和牛第三个出，士和炮继续抱头。
