import torch

w = torch.tensor([1.], requires_grad=True)
x = torch.tensor([2.], requires_grad=True)
# y=(x+w)*(w+1)
a = torch.add(x, w)
b = torch.add(w, 1)
y = torch.mul(a, b)
# y求导
y.backward(retain_graph=True)
print(w.grad)
# y.backward()
# print(w.grad)