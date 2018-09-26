#!/usr/bin/env ruby

require 'openssl'
require 'base64'
require 'timeout'
require 'securerandom'

$stdout.sync = true
Flag = ""
CHALLENGES = 100
KEY_PATH = ""

def hellomsg()
    puts "===================================================================="
    puts "Service will provide public key of RSA."
    puts "Followed by secrect msg encrypted by it!"
    puts "Challenger should give back the plaintext , p and q(which N=pq; p>q)"
    puts "There are #{CHALLENGES} rounds. Good luck and have fun!"
    puts "====================================================================\n\n"
end

def check(key, m)
    puts "msg :"         
    return false if gets.chomp != m
    puts "p (decimal) :" 
    return false if gets.chomp.to_i != key.params()["p"]
    puts "q (decimal) :" 
    return false if gets.chomp.to_i != key.params()["q"]
    return true
end

def enc(key, m)
    puts "", key.to_pem
    puts "secrect msg :#{Base64.strict_encode64(key.public_encrypt(m))}"
end

def last_round()
    puts "Last round is so called wiener's attack"
    rsa_priv = OpenSSL::PKey::RSA.new File.read KEY_PATH
    rsa_pub = rsa_priv.public_key
    m=SecureRandom.hex(n=32)
    enc(rsa_pub, m)
    exit if check(rsa_priv, m)==false
    puts Flag
end

begin
    hellomsg()
    res = Timeout.timeout(3600) do
        CHALLENGES.times do |i|
            puts "Round (#{i+1}/#{CHALLENGES})"
            rsa_priv = OpenSSL::PKey::RSA.new(CHALLENGES+i)
            rsa_pub = rsa_priv.public_key
            m=SecureRandom.hex(n=1)
            enc(rsa_pub, m)
            exit if check(rsa_priv, m)==false
        end
        last_round()
    end
rescue Timeout::Error
    puts "Toooooooooooooooooo Slow!!!!!!!!!!!!!"
end
