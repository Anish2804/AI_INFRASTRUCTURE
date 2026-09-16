# Virtualization & Virtual Machines (VMs)

## 1. Virtualization kya hai?

**Virtualization** ek technology hai jisme ek hi physical computer ke hardware resources:

* RAM
* CPU
* Storage

ka use karke **multiple Operating Systems** run kiye ja sakte hain.

---

## 2. Hypervisor ki Role

**Hypervisor** ek software hai jo virtualization ko possible banata hai.

Ye main/physical machine ke resources ko different parts mein divide karke **Virtual Machines (VMs)** create karta hai.

**Example:** Oracle VirtualBox

---

## 3. Virtual Machine (VM) kaise kaam karti hai?

Har VM ek **mini computer** ki tarah kaam karti hai.

VM **isolated** hoti hai.

Matlab:

> Ek VM mein hone wali problem normally main (host) machine ko affect nahi karti.

---

## 4. Types of Hypervisor

### Type 2 — Hosted Hypervisor

* Main Operating System (jaise Windows) ke upar install hota hai.
* Example: Oracle VirtualBox

```text
Hardware
   ↓
Host OS
   ↓
Type 2 Hypervisor
   ↓
VM
```

### Type 1 — Bare Metal Hypervisor

* Directly hardware par install hota hai.
* Iske liye alag Host OS ki zarurat nahi hoti.
* Servers mein use hota hai.
* Examples:

  * VMware vSphere
  * Citrix XenServer

```text
Hardware
   ↓
Type 1 Hypervisor
   ↓
VM
```

### Type 1 vs Type 2

| Type 1                    | Type 2                                     |
| ------------------------- | ------------------------------------------ |
| Directly hardware par     | Host OS ke upar                            |
| Host OS ki zarurat nahi   | Host OS required                           |
| Servers mein use hota hai | Desktop environments mein use ho sakta hai |

---

## 5. Virtualization ke Benefits

### 1. Cost & Space Saving

Multiple machines ko ek hi physical hardware par run kiya ja sakta hai.

### 2. Scalability

Requirement ke according resources ko **increase ya decrease** karna easy hota hai.

### 3. Maintenance

Cloud providers jaise **AWS** security aur updates ka responsibility lete hain, jisse company ka maintenance work easy ho jata hai.

---

# Quick Revision

* **Virtualization** → Ek physical computer par multiple OS run karna.
* **Hypervisor** → VMs create karta hai aur hardware resources manage/divide karta hai.
* **VM** → Ek isolated mini computer.
* **Type 2** → Host OS ke upar run hota hai.
* **Type 1** → Directly hardware par run hota hai.
* **Type 1** → Servers mein use hota hai.
* Virtualization ke benefits → **Cost/Space Saving + Scalability + Easier Maintenance**.
