�
    zΟg�  �            	       �   � d dl mZmZ dedefd�Zdeeeef                  deeeef                  deeeef                  defd�Zd	S )
�    )�List�Tuple�input_dictionary�returnc                 �>  � | d         }| d         }| d         }| d         }||k    rt          d�  �         g S |dk    rg S ||k    r||}}dg|z  }||z
  |z  }|D ]B}||cxk     r|k     r3n �t          ||z
  |z  �  �        }||k    r|dz  }||xx         dz  cc<   �C|S )N�data�n�min_val�max_valz-Error: min_val and max_val are the same valuer   �   )�print�int)	r   r   r	   r
   r   �hist�w�value�	bin_indexs	            �uc:\Users\Ateendra\OneDrive\Documents\GitHub\ecedatascience-spring2025-homework-2-s25-Homework2Spring2025\homework2.py�	histogramr      s  � �" �F�#�D����A��y�)�G��y�)�G� �'����=�>�>�>��	� 	�A�v�v��� ����"�G��� �3��7�D� 
�7�	�a��A� � %� %���U�$�$�$�$�W�$�$�$�$�$��U�W�_��1�2�2�I��A�~�~��Q��	��Y����1�$������K�    �person_to_day�person_to_month�person_to_yearc                 �   � d S )N� )r   r   r   s      r   �combine_birthday_datar   H   s	   � � 	�Dr   N)	�typingr   r   �dict�listr   �strr   r   r   r   r   �<module>r       s�   �� � � � � � � � �:	�� :	�� :	� :	� :	� :	�J
	��e�C��H�o�)>� 
	�+/��c�3�h��+@�
	�*.�u�S�#�X��*?�
	�DH�
	� 
	� 
	� 
	� 
	� 
	r   