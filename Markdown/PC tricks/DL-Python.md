**之前我在anaconda的base环境中装了别的包，想要卸载回退到最开始的样子**

``` powershell
conda list --revisions
conda install --rev 0
```

**查看远程的服务器显卡的使用情况**

``` powershell
nvidia-smi
```

**使用特定的显卡运行程序**

``` python
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '1'
```

