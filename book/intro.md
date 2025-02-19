(intro)=
# Welcome to the Template Book

_This is the first page the student will see when opening the url._

This book can be used as a template for other books. It includes a starter package of the software developed by the TeachBooks initiative and some exercises to get you going!

[Jupyter Book](https://jupyterbook.org)


### Contents

1. Mathematical Preliminaries  
   1.1 Overview  
   1.2 Algebra of Vectors  
   1.3 Algebra of Second-Order Tensors  
   1.4 Algebra of Fourth-Order Tensors  
   1.5 Eigenvalues, Eigenvectors of Tensors  
   1.6 Transformation Laws  
   1.7 Scalar, Vector, Tensor Functions  
   1.8 Gradients and Related Operators  
   1.9 Integral Theorems  
   1.10 Summary  

---

# Chapter 1: Mathematical Preliminaries

## 1.1 Overview

Some quantities like force are vectors (first-order tensors), and stress is a second-order tensor. The algebra and calculus of tensors differ in some aspects from scalar quantities. This lecture covers equations involving vectors and tensors and how to take derivatives of scalar-valued functions of tensors and tensor-valued functions of tensors.

## 1.2 Algebra of Vectors

A scalar is a physical quantity described by a single real number (e.g., temperature, mass). A vector is a directed line element in space used to model quantities such as force, velocity, and acceleration. Vectors are represented as:

```
**v** = v1 e1 + v2 e2 + v3 e3
```

where **e1, e2, e3** are basis vectors. The magnitude of a vector is:

```
|v| = sqrt(v1^2 + v2^2 + v3^2)
```

### Vector Addition

Vector addition follows the parallelogram law and satisfies:

```
u + v = v + u
(u + v) + w = u + (v + w)
```

### Scalar Multiplication

```
(αβ)u = α(βu)
(α + β)u = αu + βu
```

### Dot Product

```
u · v = u1v1 + u2v2 + u3v3
```

### Cross Product

```
u ∧ v = |u||v| sin(θ) n
```

where **θ** is the angle between **u** and **v**, and **n** is a unit vector normal to the plane they span.

---

## 1.3 Algebra of Second-Order Tensors

A second-order tensor **A** maps a vector to another vector:

```
v = A u
```

#### Properties:
```
(A + B)u = A u + B u
(αA)u = α(A u)
```

#### Transpose:
```
(A^T)_{ij} = A_{ji}
```

#### Trace and Determinant:
```
tr(A) = A_ii

det(A) = ϵ_ijk A_i1 A_j2 A_k3
```

---

## 1.4 Algebra of Fourth-Order Tensors

A fourth-order tensor maps a second-order tensor to another second-order tensor. If **A** is a fourth-order tensor, then:

```
B = A : C
```

where `:` denotes double contraction.

---

## 1.5 Eigenvalues, Eigenvectors of Tensors

For a tensor **A**, the eigenvalues λ_i satisfy:

```
A n̂_i = λ_i n̂_i
```

where **n̂_i** are the eigenvectors.

#### Characteristic Equation:
```
λ^3 - I1λ^2 + I2λ - I3 = 0
```

where **I1, I2, I3** are invariants of **A**.

---

## 1.6 Transformation Laws

Given two coordinate systems with basis vectors **e_i** and **ẽ_i**, the directional cosine matrix **Q** is defined as:

```
Q_ij = e_i · ẽ_j
```

The transformation laws for vectors and tensors are:

```
ũ_j = Q_ij u_i
Ã_ij = Q_ai Q_bj A_ab
```

---

## 1.7 Scalar, Vector, Tensor Functions

A function assigns values to elements of a domain:

```
Φ = Φ̂(x)
```

### Differentiability

A scalar field Φ(x) is differentiable if there exists a vector **grad(Φ)** such that:

```
lim_{α → 0} |grad(Φ) · a - α^{-1}[Φ(x + αa) - Φ(x)]| = 0
```

---

## 1.8 Gradients and Related Operators

For a scalar field **Φ(x)**:

```
grad(Φ) = (∂Φ/∂x) e1 + (∂Φ/∂y) e2 + (∂Φ/∂z) e3
```

For a vector field **u(x)**:

```
∇u = (∂u_i/∂x_j) e_i ⊗ e_j
```

---

## 1.9 Integral Theorems

#### Divergence Theorem
```
∫_V ∇ · F dV = ∮_{∂V} F · dS
```

#### Stokes' Theorem
```
∮_C F · dr = ∫_S (∇ × F) · dS
```

#### Green's Theorem
```
∫_D (∂Q/∂x - ∂P/∂y) dA = ∮_{∂D} (P dx + Q dy)
```

---

## 1.10 Summary

This document covers vector algebra, tensor algebra, transformation laws, tensor calculus, and integral theorems.

---

**End of Document**
