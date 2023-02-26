# 												ANLY-580 Assignment-01

**Your name**: Jieyi Sun

**Your NET ID**: js4958

**Teammates:** Jieqian Liu, Sirui Wang

## Problems

1. (10 pts) Establish the convexity of the following functions, showing any necessary derivation steps.

    a. $f(x) = x^{2}$

    b. $f(x) = \ln(x)$

    c. $f(x) = \frac{1}{1 + e^{-x}}$

    *Hint: convexity is non binary, some functions are neither convex nor concave, some are convex/concave over finite intervals etc..* 
    
    
    
    a. $f^`(x)=2x$
    
    ​	$f^{``}(x)=2>0$
    
    ​	So this function is convex.
    
    b. $f^`(x)=1/x$
    
    ​	$f^{``}(x)=-1/x^2<0$
    
    ​	So this function is not convex.
    
    c. $f^`(x)=e^{-x}/(1+e^{-x})^2$
    
    ​	$f^{``}(x)=(e^{-x}-1)e^{-x}/(1+e^{-x})^3$
    
    ​	when $x>0$, $f^{``}(x)>0$ , $f(x)$ is convex.
    
    ​	when $x\leq0$, $f^{``}(x)\leq0$ , $f(x)$ is not convex.
    
    
    
2. (10 pts) Consider a continuous random variable $X$ that is drawn from a uniform distribution between the values $0$ and $\theta$. Please compute the following, showing each derivation step:

    a. $\mathbb{E}_{X}[X]$

    b. $\text{var}(X)$ 

    c. $H(X)$

    *Note:* $H(X)$ *denotes the [entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)) of* $X$. 
    
    
    
    $f(X)=1/\theta$
    
    a. $E_X(X)=\int_0^\theta x\frac{1}{\theta}dx=\frac{\theta}{2}$
    
    b. $var(X)=E(X^2)-[E(X)]^2=\frac{\theta ^2}{3}-\frac{\theta ^2}{4}=\frac{\theta ^2}{12}$
    
    c.$H(X)=-log\frac{1}{\theta}=log\theta$
    
    


3. (40 pts) Given $M$ independently drawn samples of $X$ from (2), $x_{1}, ..., x_{M}$, compute the maximum likelihood estimate of $\theta$, $\hat{\theta}$. Please show the steps to arrive at this answer.

   

   Likelihood function is $L(\theta|x)= \prod^M_{i=1}\frac{1}{\theta}=\theta ^{-n}$

   $\frac{dlnL(\theta|x)}{d\theta}=-\frac{n}{\theta}<0$

   So this function decrease when $\theta$ increases. Therefore, the maximum likelihood estimate $\hat\theta=x_M=max\{x_1,x_2,...,x_M\}$



4. (20 pts) Imagine you are given the choice of three sound proof doors: Behind one door is \$1M cash; behind the others, crickets. After making your choice (but not observing the outcome), an omnicient host reveals crickets behind one of the other doors. The host then asks you the following: *Would you like to switch doors?* Using Bayes' Rule, determine whether or not you should switch doors to maximize your chances of winning $1M.

   

   Suppose: A、B、C are the three doors. X means the chosen door; Y means the door opened by host; Z means the door having cash.

   ​		P(Z=A)=P(Z=B)=P(Z=C)=$\frac{1}{3}$

   ​		P(X=A,Y=B|Z=A)=$\frac{1}{2}$, P(X=A,Y=B|Z=B)=0, P(X=A,Y=B|Z=C)=1

   ​		P(X=A,Y=B)=$\frac{1}{2}$·$\frac{1}{3}$+0·$\frac{1}{3}$+1·$\frac{1}{3}$)=$\frac{1}{2}$

   ​		Therefore, P(Z=A|X=A,Y=B)=$\frac{(1/2)·(1/3)}{1/2}=\frac{1}{3}$, P(Z=B|X=A,Y=B)=$\frac{0·(1/3)}{1/2}=0$,  P(Z=C|X=A,Y=B)=$\frac{1·(1/3)}{1/2}=\frac{2}{3}$

   So, when you chose door A initially and the host open door B, the probability of cash behind the door C is highest. So you should choose to switch the door.	



5. (20 pts) Consider the covariance matrix, $\Sigma \in \mathbb{R}^{N \times N}$ of a random vector $X \in \mathbb{R}^{N}$. Show that $\Sigma$ is a positive semidefnite matrix. What are some of the implications of $\Sigma$ being PSD?
   *Note: The covariance of $X$ is defined as $\Sigma = \mathbb{E}_{X}\big[ \big( X - \mathbb{E}_{X}[X] \big)\big( X - \mathbb{E}_{X}[X] \big)^{T} \big]$*

   

   If $\Sigma$ is positive semidefinite, let u be a random vector, hence:

   $\mu^T\Sigma \mu=\mu^TE_{X}\big[ \big( X - E_{X}[X] \big)\big( X - E_{X}[X] \big)^{T} \big]\mu=E[\mu^T( X - E_{X}[X] \big)\big( X - E_{X}[X] \big)^{T}\mu]=E(s^2)\sigma_s^2 >=0$
   
   $\sigma_s^2$ is the covariance of the zero-mean normalize random variable s.
   
   If $\Sigma$ is positive semidefinite matrix (PSD), there must be $\mu^T\Sigma \mu\geq0 ,$  So  $\sigma _s^2\geq0$