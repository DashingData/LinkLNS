echo [$(date)]: "START"
# Yeh line script ke shuru hone ka time print karta hai, jo debugging mein madad karta hai

echo [$(date)]: "Create conda env using python 3.9"
# Yeh line batata hai ki hum Python 3.9 ke saath ek naya conda environment bana rahe hain

conda create --prefix ./env python=3.9 -y
# Yeh command current directory mein 'env' naam se ek naya conda environment banata hai, Python 3.9 ke saath
# '-y' flag automatically 'yes' answer deta hai, jisse process automated ho jata hai

echo [$(date)]: "Activate conda env"
# Yeh line batata hai ki ab hum naye banaye gaye environment ko activate kar rahe hain

source activate ./env
# Yeh command naye banaye gaye conda environment ko activate karta hai

pip install -r requirements_dev.txt
# Yeh command requirements_dev.txt file mein listed saare packages ko install karta hai

echo [$(date)]: "END"
# Yeh line script ke khatm hone ka time print karta hai, jo execution time calculate karne mein madad karta hai
