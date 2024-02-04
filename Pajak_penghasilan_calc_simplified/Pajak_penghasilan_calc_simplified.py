'''
- According to Pemotongan Pajak Penghasilan PPh Pasal 21 Tahun 2016, we can calculate our income tax as (we'll write in Bahasa Indonesia for avoiding missinterpretation)

- **Penghasilan tidak kena pajak (PTKP)**
  - Penghasilan Rp 54.000.000 setahun untuk wajib pajak.
  - Tambahan Rp 4.500.000 diberikan jika wajib pajak menikah.
  - Tambahan Rp 4.500.000 lagi jika punya 1 orang anak atau Rp 9.000.000 jika punya 2 orang anak. Apabila jumlah tanggungan lebih dari itu, maka tetap dihitung 3 orang tanggungan.

- **Tarif Pajak Penghasilan**
  - 5% untuk penghasilan kena pajak (PKP) sampai dengan 60 Juta
  - 15% untuk PKP di atas 60 juta sampai dengan 250 Juta
  - 25% untuk PKP di atas 250 juta sampai dengan 500 juta
  - 30% untuk PKP di atas 500 juta sampai dengan 5 miliar
  - 35% untuk PKP di atas 5 miliar

- Your task is calculate the income tax given
  - Monthly income
  - Marital status
  - The number of dependents (jumlah tanggungan)
'''
# input value for monthly income, marrital status, & total dependents
monthly_income = 15000000
marital_status = 'married'
n_dependents = 3

# get annualy income value
annual_income = monthly_income * 12

# calculate 'Penghasilan tidak kena pajak (PTKP)'
if marital_status == 'married': # for married category
  if n_dependents == 0: # for married category with zero kids
    ptkp = 54000000 + 4500000
  else: # for married category with kids
    if n_dependents <= 3: # for married category with less than 3 kids
      ptkp = 54000000 + 4500000 + (4500000 * n_dependents)
    else: # for married category with more than 3 kids
      ptkp = 54000000 + 4500000 + (4500000 * 3)
elif marital_status == 'single': # for single category
  ptkp = 54000000

# calculate 'Penghasilan Kena Pajak (PKP)'
pkp = annual_income - ptkp

# calculate 'PPH 21' with 'Tarif Pajak Penghasilan (TPP)'
if pkp <=60000000: # for TPP below Rp. 60.000.000
  pph = pkp * 0.05
elif pkp <= 250000000: # for TPP Rp. 60.000.000 - Rp. 250.000.000
  pph = pkp * 0.15
elif pkp <= 500000000: # for TPP Rp. 250.000.000 - Rp. 500.000.000
  pph = pkp * 0.25
elif pkp <= 5000000000: # for TPP Rp. 500.000.000 - Rp. 5.000.000.000
  pph = pkp * 0.3
else: # for TPP more than Rp. 5.000.000.000
  pph = pkp * 0.35

# show output value
print(f'Penghasilan neto setahun:\n{annual_income}')
print(f'\nPTKP TK/{n_dependents}:\n-{ptkp}')
print(f'\nPenghasilan Kena Pajak:\n{pkp}')
print(f'\nPPh 21 terutang setahun:\n{int(pph)}')