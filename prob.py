k, n, m = 2.0, 2.0, 2.0
t = k + m + n 
##
## Probability of selecting mating pairs
## 
    
##
## Selection of first mating organism
##
    
k_odds, m_odds, n_odds = (k/t), (m/t), (n/t)
    
##
## Selection of second mating organism
##
    
kk_odds, km_odds, kn_odds = (k-1)/(t-1), (m)/(t-1), (n)/(t-1)
mm_odds, mk_odds, mn_odds = (m-1)/(t-1), (k)/(t-1), (n)/(t-1)
nn_odds, nk_odds, nm_odds = (n-1)/(t-1), (k)/(t-1), (n)/(t-1)
    
##
## Punnett square odds for dominant phenotype
##
##  two_homo_dominant = MM x MM = (4/4)
##   two_heterozygous = Mm x Mm = (3/4)
## two_homo_recessive = mm x mm = (0/4)
##      dom_recessive = MM x mm = (4/4)
##    hetero_homo_dom = Mm x MM = (4/4)
##    hetero_homo_rec = Mm x mm = (1/2)
    
two_homo_dominant, two_heterozygous, two_homo_recessive, dom_recessive, hetero_homo_dom, hetero_homo_rec = 1.00, 0.75, 0.00, 1.00, 1.00, 0.50

prob = {
        'first_round'     : [k_odds, m_odds, n_odds],
        0  : [kk_odds, km_odds, kn_odds],
        1  : [mm_odds, mk_odds, mn_odds],
        2  : [nn_odds, nk_odds, nm_odds]
}