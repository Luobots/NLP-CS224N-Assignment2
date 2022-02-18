##任务二：word2vec实现 (1 week)

__参考__ ：我们提供了BP的参考资料
__环境__ ：在Python下配置jupyter/matplotlib/numpy/python=3.7/scikit-learn；我们提供了conda的env.yml
__要求__ ：实现word2vec并使用sgd进行模型学习，获得词向量

- word2vec模型实现 (word2vec.py)：完成后，通过运行python word2vec.py进行测试。
  1. 完成sigmoid函数
  2. 完成其中的softmax和negative sampling函数的LossAndGradient函数
  3. 完成skiggram函数
- 在sgd.py中完成SGD优化器的实现。完成后，通过运行python sgd.py进行测试。
- 加载实际数据并训练词向量：我们使用SST数据集来训练词向量，然后将其应用于情感分析任务（不需要写代码）。
  1. 获取数据集：运行sh get datasets.sh
  2. 进行训练：运行python run.py
     注意：训练过程可能需要很长时间，具体取决于机器速度（大约需要一个小时）。经过40,000次迭代，训练完成，脚本将对词向量进行可视化并把图像输出到word vectors.png。写一份报告介绍你的观察结果。
